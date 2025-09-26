========
Overview
========

Action Runner
=============

The action runner (core-automation) is responsible for:

#. Sequencing (ordering) actions
#. Executing actions (in order)
#. Monitoring executed actions for completion of failure.

It is an abstraction on top of various API calls, designed to separate the **authoring** of data (i.e. CloudFormation templates) from the **execution** of that data (i.e. creating a Cloudformation stack).

Repository layout
=================

* ``bin/`` - scripts to deploy the action runner, as well as additional automation scripts.
* ``cloudformation/`` - CloudFormation templates for deploying the action runner
* ``lambdas/`` - code for the various Lambda functions in this project
* ``docs/`` - sphinx documentation files

Actions
=======

The input to the action runner is a list (array) of JSON-encoded action objects, with a structure like::

    [
        {
            "label": "create-network-sin",
            "depends_on": [ "create-network-syd" ],
            "type": "aws.create_stack",
            "params": {
                "stack_name": "core-network",
                "template_url": "https://s3-ap-southeast-1.amazonaws.com/core-automation/artifacts/core/network/master/a1b2c3d4/network.yml",
                "region": "ap-southeast-1",
                "account": 227367769952,
                "tags": [
                    { "Key": "project", "Value": "core" },
                    { "Key": "app", "Value": "network" }
                ]
            }
        },
        (etc)
    ]


Available actions
=================

For all actions, see :doc:`actions`.

Action Ordering
===============

Actions can be sequenced through a dependency chain system using the keyword `depends_on`. An action will be executed as soon as all of the listed dependencies have completed. Multiple actions can be run in parallel.

Flow Control
============

The action runner provides a `flow_control` output variable which instructs the orchestrating system of which state to transition to next (eg: wait, success, failure, re-execute)
This was designed with Step Functions in mind, where the step function can wait and return execution to the Lambda after some amount of time.

Execution Environment
=====================

The runner was built to run inside the constraints of AWS Lambda and Step Functions:

* Lowest memory possible - 128MB is targetted, but up to 1.5GB is possible with cost implications.
* Maximum 5 minute execution time - will exit after 5 minutes with a flag showing it requires further execution
* Input / output size - Lambda has a 128KB input / output limit, and step functions has a 32KB input / output limit. Large lists of actions are possible and expected, but cannot be provided as a Lambda payload due to size constraints. For this reason, actions and state are published to a versioned S3 bucket. The version id ensures read-after-write consistency.
* 512MB scratch disk space - Lambda provides a 512MB /tmp mount
* Logging - logging should include relevant execution details so multiple intertwined logs can be split into their respective threads. Lambda uses the Python logger for its own purposes, so this cannot be cleanly used for our logging.

Asynchronous Execution
======================

Since this runs on Lambda with a maximum execution time of 5 minutes, action execution needs to be asynchronous (ie: no long waits). The action runner then performs a check of the status of the executed action on its next invocation.

Running Outside of Lambda
=========================

Being Python, the effort to modify this code and execute it outside of Lambda should be minimal. The hander function at the top level of each Lambda function conatin the only Lambda-specific interaction (even then, it's simply a method with specific inputs and outputs)

Pipeline?
=========

Actions are designed to be a basic instruction set for performing tasks. Any higher level specification files (as seen in deployment pipeline systems) will need be compiled into a list of actions to be executed.

In this model, a "pipeline" is responsible for compiling high level specification files into a list of actions for this action runner to then accept and execute, taking care of action ordering, execution, rollback, logging, etc. This effectively separates two concerns - processing (compiling) the spec file, and executing the actions.

What Next?
==========

* Look at :doc:`getting_started` for setting up your own environment (optionally with your own aws account).
* Try :doc:`deploying_apps` and deploy the canary app from your machine.
* Read through the documentation for each lambda.
* Read :doc:`deploying_automation` for info about updating ``core-automation`` itself.

