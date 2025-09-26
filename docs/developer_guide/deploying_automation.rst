=========================
Deploying Core Automation
=========================

Currently, the runner itself (core-automation) is deployed/updated using deployment scripts. These scripts can be triggered from a developer laptop with sufficient AWS privileges, or from a CI/CD tool such as Jenkins.

Manual deployment
=================

Checkout the following repositories:

* core-automation
* [client]-config (eg: abc-config)

The deployment script resides in the core-automation repository under ``bin/deploy.sh``. Similarly, a teardown script resides in ``bin/teardown.sh``.

Getting script help
-------------------

.. code-block:: bash

    bash ./bin/deploy.sh --help

Building the documentation
--------------------------

.. code-block:: bash

    python3 ./bin/install-lambda-dependencies.py
    cd docs
    make html

Running deployment
------------------

.. code-block:: bash

    AWS_PROFILE=automation \
    bash ./bin/deploy.sh --client abc --branch testing --build 1

* Where ``AWS_PROFILE=automation`` selects the AWS profile with required privileges to deploy the automation

Running teardown
----------------

.. code-block:: bash

    AWS_PROFILE=automation \
    bash ./bin/teardown.sh -c abc -b testing -n 1

* Where ``AWS_PROFILE=automation`` selects the AWS profile with required privileges to teardown the automation

.. _automated-deployment:

Automated Deployment (with AWS CodeBuild)
=========================================

Another option used at client sites is to use CodeCommit and CodeBuild together to deploy core-automation.

Setting up your AWS environment
-------------------------------

Use a deployspec repo (e.g. core-codecommit) to setup the required resources. Example:

.. literalinclude:: ./samples/core-automation-resources.yaml
  :language: yaml
  :caption: Cloudformation Resources For Core Automation CD

Note in the above example, only certain branches of core-automation are continuously deployed.

Local repos required
--------------------

1) Facts repo
2) Core automation repo
3) demo-app, demo-canary repos are handy for testing

Local development process
-------------------------

1) Create branch in facts repo that aligns with the name of your core-automation branch (e.g. "dev"). Push it up and let facts be CD'd to s3.
2) Ensure the relevant branch of demo-canary is available - it will be used as a "smoke test" before deployment.
3) Create branch of core-automation. Do your work there.
4) Test your work by compiling locally first, to ensure that step works as expected.
5) Push your branch. If it's ci/cd branch, it will be deployed to AWS automatically, ready to be used.
6) When you're happy that you can deploy, release and teardown demo-apps and demo-canaries with your changes, raise a core-automation PR into master. Once the CCoE team reviews and merges, the CI/CD process will kick-in and deploy. Documentation will be updated as well!

Deploy, release, teardown and app using your branch of core-automation
----------------------------------------------------------------------

Here's an example using ``--invoker-branch mergeforward`` to use your deployed branch of core-automation:

.. code-block:: bash

    AWS_PROFILE=client-automation ../core-automation/bin/run.sh package upload compile deploy --invoker-branch mergeforward -c client -p demo -a app -b single -n 500
    AWS_PROFILE=client-automation ../core-automation/bin/run.sh release --invoker-branch mergeforward -c client -p demo -a app -b single -n 500
    AWS_PROFILE=client-automation ../core-automation/bin/run.sh teardown --invoker-branch mergeforward -c client -p demo -a app -b single -n 500
