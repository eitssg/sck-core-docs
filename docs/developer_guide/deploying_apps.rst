==============
Deploying apps
==============

This section covers commands to deploy applications both from a local machine and by invoking the automation Lambdas in AWS.

End-to-end deploy
=================

Getting help
------------
Run from the core-automation repository directory.

.. code-block:: bash

    core --help

Package, upload, compile, deploy the app
----------------------------------------
Run from the demo-canary repository directory.

.. code-block:: bash

    AWS_PROFILE=abc-automation \
    core package upload compile deploy -c abc -p demo -a canary -b mybranch -n 1

* This is the same command run by the CI/CD tool
* The compile and deploy steps will trigger the deployed Lambdas in AWS


Local compilation
=================

Getting help
------------
Run from core-automation compilers.

.. code-block:: bash

    core compile --help


Local compile of local files
----------------------------

* Will compile the app specified by --app-path

.. code-block:: bash

    core compile -p abc -a demo -b canary -n 1 --mode local --app-path ~/workspace/demo-canary


Local compile of S3 files
-------------------------
* Will compile the app by downloading package from S3 and uploading compiled artefacts to S3

.. code-block:: bash

    core compile -c abc -p demo -a canary -b mybranch -n 1 --mode s3 --aws-profile abc-automation

Local action execution
======================

Local deploy
------------

Run from simple-cloud-kit/sck-core-execute directory.

.. code-block:: bash

    core deploy -c abc -p demo -a canary -b mybranch -n 1 --aws-profile abc-automation --dry-run

Where:

* **deploy** - action to run
* **demo** - portfolio name
* **canary** - app name
* **mybranch** - branch name
* **1** - build number
* **abc-automation** - AWS credentials profile with sufficient privileges to deploy


Local teardown
--------------

Teardown action (wise to run BEFORE, if you're re-deploying the same build number)

.. code-block:: bash

    core teardown -c abc -p demo -a canary -b mybranch -n 1 --aws-profile abc-automation --dry-run

Where:

* **teardown** - action to run
* **demo** - portfolio name
* **canary** - app name
* **mybranch** - branch name
* **1** - build number
* **abc-automation** - AWS credentials profile with sufficient privileges to teardown

Deploying apps using different branches of core-automation
==========================================================

If you're continuously deploying branches of core-automation as per :ref:`automated-deployment`, you can also configure apps to be deployed with different branches of core-automation.

This is especially useful when building new Consumables or adding new features to the automation platform that you need to test.

Steps (assuming you use CodeCommit & CodeBuild. For other systems, check their documentation):

#. Clone ``$client-config`` (facts repo), ``core-automation``, ``core-codecommit``, and ``demo-app`` repos.
#. In core-codecommit, update your "CoreAutomationRepo" trigger to add your new core-automation branch to CI/CD. Don't push yet.
#. In core-codecommit, update deployspec.yaml, add/update "CodeCommitListenerLambdaArn" and "InvokerLambdaArn":

   .. code-block:: yaml

       - label: deploy-portfolio-demo
         type: create_stack
         params:
           template: portfolio-demo.yaml
           stack_name: "{{ core.Project }}-{{ core.App }}-portfolio-demo"
           parameters:
             CodeCommitListenerLambdaArn: arn:aws:lambda:ap-southeast-1:123456789012:function:core-automation-alblambda-codecommit  # From "master"
             InvokerLambdaArn: arn:aws:lambda:ap-southeast-1:123456789012:function:core-automation-*-invoker  # Allow any branch of the invoker!
             S3Bucket: CLIENT-core-automation-ap-southeast-1
             RunZipS3Key: artefacts/core/automation-runner/alblambda/_latest/run.zip
             CodeBuildImage: 123456789012.dkr.ecr.ap-southeast-1.amazonaws.com/core-codecommit-mini:latest
           accounts:
             - "123456789012"  # automation account
           regions:
             - ap-southeast-1  # Asia Pacific (Singapore)

#. Update your app definitions in ``core-codecommit`` to make use of ``INVOKER_BRANCH`` environment variable:

   .. code-block:: yaml

        EnvironmentVariables:
          - { Name: INVOKER_BRANCH, Type: PLAINTEXT, Value: 'master' }
        # Buildspec lines:
        # - ./run.sh package upload compile deploy -c $CLIENT -p $PORTFOLIO -a $APP -b $BRANCH -n $BUILD_NUMBER --invoker-branch $INVOKER_BRANCH
        # - ./run.sh release -c $CLIENT -p demo -a app -b $BRANCH -n $BUILD_NUMBER --invoker-branch $INVOKER_BRANCH
        # - ./run.sh teardown -c $CLIENT -p demo -a app -b $BRANCH -n $BUILD_NUMBER --invoker-branch $INVOKER_BRANCH

#. PR core-codecommit into master, let CI/CD deploy your updates.
#. Update ``$client-config/appls.yaml`` facts, add a definition for a branch of demo-app. Push. Example:

   .. code-block:: yaml

        prn:demo:app:serverless:*:
          Account: nonprod-auto
          Region: sin
          InvokerBranch: alblambda


#. Create a branch of demo-app, create your new component definitions etc, and push.

With the above, CodeCommit for demo-app will trigger your branch of CodeCommitListenerLambdaArn, which will lookup facts and then invoke demo-app CodeBuild project (using InvokerBranch fact for INVOKER_BRANCH env var), and the CodeBuild project will pass ``--invoker-branch $INVOKER_BRANCH`` to run.sh and awayyyy we go! Your branch's core-automation lambdas are now invoked for this application.

A good use of demo-canary, to test in cloud before merging core-automation to master and making your feature available to all.
