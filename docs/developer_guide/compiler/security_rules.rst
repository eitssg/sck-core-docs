======================
Security Items & Rules
======================

Overview
========

TBC

Two-Step Security Rules Creation
================================

See bitbucket (pull-requests/16/aws-sqs-queue-consumable-fixes/diff)

This change is to cater for security rules that reference resources with randomness injected into their names (eg: sqs queues).

Previously, we always created the security rules stack **before** the resources stack and got away with it because we could predict all resource arns before the resources were actually created (eg: we can predict a dynamodb table's ARN by setting the table name).

Ok so, great, we'll just create the security rules stack after the resources stack so that we know the resource name! All good - **except** that the security rules stack also contains any default rules such as allowing instances to access S3 files, without which cfn-init will fail and the stack will fail. So what we're doing now is:

#. Create the security rules stack with ``ResourcesStackName`` is set to blank (""), to create all base rules.
#. Create the resources stack
#. Update the security rules stack with ``ResourcesStackName`` set, to create the remaining rules for dynamically named resources.

To achieve this, ``Condition: ResourcesExist`` is used on any rules resources that will try to import values from the resources stack.

.. todo::

    Now that we have this, we should probably also let the DynamoDB table be dynamically named by CFN in the event that someone creates a long branch name and exceeds the table name length limit (we concatenate portfolio, app, branch, build, component to create the table name)
    Maybe even lambda function names..limited to 64 characters