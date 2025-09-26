..  _pipeline-functions:

==================
Pipeline functions
==================

Fn::Pipeline::DockerImage
=========================

Retrieve a Docker image name from an alias

.. code-block:: yaml
    :caption: Snippet: specifying an image id for an instance

    ...
    ImageId:
      Fn::Pipeline::DockerImage:
        Name: base/rhel7
    ...

Properties
----------
**Name**
    Short name of the image.

    * **Required**: Yes
    * **Type**: String

Fn::Pipeline::FileS3Key
=======================

Retrieve the S3 key of a user file.

.. code-block:: yaml
    :caption: Snippet: specifying a file for use by AWS Lambda

    ...
    Function:
      Properties:
        Code
          S3Key:
            Fn::Pipeline::FileS3Key:
              Path: "my-function.zip"
    ...

Properties
----------
**Path**
    Path of the file.

    The path is relative to the *files* directory in your repository.

    * **Required**: Yes
    * **Type**: String

Fn::Pipeline::FileUrl
=====================

Retrieve the URL of a user file.

.. code-block:: yaml
    :caption: Snippet: specifying a file in cfn-init metadata

    ...
    AWS::CloudFormation::Init:
      config:
        files:
          /opt/my-file.jar:
            source:
              Fn::Pipeline::FileUrl:
                Path: "mycomponent/my-file.jar"
    ...

Properties
----------
**Path**
    Path of the file.

    For *build* scope, this will be relative to the *files* directory in your repository.

    * **Required**: Yes
    * **Type**: String

**Scope**
    Scope of the file.

    **Note**: Files uploaded from the *files* directory of your repository are in the *build* scope.

    * **Default**: build
    * **Valid values**: shared, portfolio, app, branch, build
    * **Required**: No
    * **Type**: String

.. Fn::Pipeline::GeneratePassword
.. ==============================

.. Generate a password string.

.. .. code-block:: yaml
..     :caption: Snippet: generating a database password

..     ...
..     MasterUserPassword: # Deprecated - master user password for RDS now handled internally by the consumable.
..       Fn::Pipeline::GeneratePassword:
..         Length: 16
..         CharacterSet: "a-zA-Z0-9!@#$%^&*()"
..     ...

.. Properties
.. ----------
.. **CharacterSet**
..     Set of characters to use when generating the password.

..     * **Default**: a-zA-Z0-9!@#$%^&*()
..     * **Required**: No
..     * **Type**: String

.. **Length**
..     Length of the password to generate

..     * **Required**: Yes
..     * **Type**: Number

Fn::Pipeline::GetOutput
=======================

Generate a CFN stack export name using core-automation's naming conventions. Default scope is a "build" export.

.. code-block:: yaml
    :caption: Snippet: Referencing the "mylambda" component's Lambda ARN in an ApplicationLoadBalancer component.

    DefaultTargetGroup:
      Properties:
        Targets:
          - Id:
              Fn::Pipeline::GetOutput:
                Component: mylambda
                OutputName: DeploymentAliasArn

Fn::Pipeline::ImageId
=====================

Retrieve an image id.

.. code-block:: yaml
    :caption: Snippet: specifying an image id for an instance

    ...
    ImageId:
      Fn::Pipeline::ImageId:
        Name: amazon-linux-latest
    ...

Properties
----------
**Name**
    Short name of the image.

    * **Required**: Yes
    * **Type**: String

Fn::Pipeline::LambdaVpcConfig
=============================

Configure VPC attachment for a Lambda function. Note that versions of a single
function will all share the VPC configuration of the most recently deployed
version.

.. code-block:: yaml
    :caption: Snippet: specifying VPC attachment

    ...
    VpcConfig:
      Fn::Pipeline::LambdaVpcConfig:
        VpcAccess: false
    ...

Properties
----------
**VpcAccess**
    Whether Lambda function should be attached to VPC.

    * **Required**: Yes
    * **Type**: String
    * **Default**: true

Fn::Pipeline::S3BucketName
==========================

Construct the name of an S3 bucket, based on provided parameters

.. code-block:: yaml
    :caption: Snippet: bucket name based on scope

    ...
    BucketName:
      Fn::Pipeline::S3BucketName:
        Scope: branch
    ...

Properties
----------
**Scope**
    Scope of the bucket.

    * **Default**: build
    * **Valid values**: branch, build
    * **Required**: Yes
    * **Type**: String

Fn::Pipeline::SnapshotId
========================

Resolve a semantic name to a snapshot identifier (name, arn, etc).

.. code-block:: yaml
    :caption: Snippet: specifying a snapshot for ElastiCache/Redis

    SnapshotName:
        Fn::Pipeline::SnapshotId:
            Name: DemoRedisLatest

"DemoRedisLatest" is a semantic name that is then resolved using Facts. Example:

.. code-block:: yaml
    :caption: Snippet: apps.yaml Facts example

    prn:demo:redis:*:*:
      Account: nonprod-app
      Region: sin
      AccountAliases:
        OldDev: '123456789012' # cross-account
      SnapshotAliases:
        AWS::ElastiCache::Redis:
          DemoRedisLatest:
            SnapshotIdentifier: 'demo-redis-master-106-redis-resources-snapshot-replicationgroup-l8k111112222'
        AWS::Redshift::Cluster:
          SomeSharedSnapshot:
            SnapshotIdentifier: some-old-snapshot-name
            AccountAlias: OldDev

Fn::Pipeline::SubnetId
======================

Retrieve a subnet id based on selectors.

.. code-block:: yaml
    :caption: Snippet: specifying a subnet id

    ...
    SubnetId:
      Fn::Pipeline::SubnetId:
        NetworkZone: private
        AzIndex: 0
    ...

Properties
----------
**NetworkZone**
    Name of the subnet's network zone.

    * **Required**: Yes
    * **Type**: String

**AzIndex**
    Index of the subnet's availability zone.

    * **Default**: 0
    * **Required**: No
    * **Type**: Number

Fn::Pipeline::SubnetIds
=======================

Retrieve a list of subnet ids based on selectors.

.. code-block:: yaml
    :caption: Snippet: specifying a subnet ids

    SubnetIds:
      Fn::Pipeline::SubnetIds:
        NetworkZone: private

Pipeline::Agents
================

Configures agents on EC2 instances.

.. code-block:: yaml
    :caption: Snippet: Example install awslogs agent and configure to watch custom log file

    LaunchConfiguration:
      Metadata:
        Pipeline::Agents:
          awslogs:
            Logs:
              - File: /var/log/httpd/access_log

.. code-block:: yaml
    :caption: Snippet: Example install datadog agent

    BakeInstance:
      Metadata:
        Pipeline::Agents:
          datadog:
            enabled: True

Supported Agents
----------------

awslogs
~~~~~~~

Configures the AWS CloudWatch Logs agent to monitor the specified log files.

Note: a number of system files are monitored by default, including cfn-init log files and the system messages log.

.. table:: Available Properties
    :widths: grid

    +----------+---------------+--------------------------------+
    | Property | Default Value | Comments                       |
    +==========+===============+================================+
    | Logs     |               | A list of log files to monitor |
    +----------+---------------+--------------------------------+


datadog
~~~~~~~

Configures the Datadog agent to monitor on the server

.. table:: Available Properties
    :widths: grid

    +----------+---------------+--------------------------------+
    | Property | Default Value | Comments                       |
    +==========+===============+================================+
    | enabled  |               |                                |
    +----------+---------------+--------------------------------+
