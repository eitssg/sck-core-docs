================
AWS::S3::Storage
================

.. attention:: This consumable is deprecated no longer maintained. Please use AWS::S3::Bucket instead.

Architectural Outcome
=====================

The consumable grants an S3 prefix in the automation bucket to an application allowing the user to control the permissions of the specified prefix.

The resource is configured according to properties and default set out below.

Quick Start
===========

.. literalinclude:: ../samples/s3-storage-quickstart.yaml
  :language: yaml
  :caption: AWS::S3::Storage Quick Start

Resources
=========

Prefix Configuration
--------------------

:Naming pattern: ``Storage``
:Required: Yes

.. table:: Available Properties
    :widths: grid

    +----------+---------------+-----------------------------------------------+
    | Property | Default Value | Comments                                      |
    +==========+===============+===============================================+
    | Prefix   |               | Key prefix                                    |
    +----------+---------------+-----------------------------------------------+
    | Scope    | build         | Allowed values: portfolio, app, branch, build |
    +----------+---------------+-----------------------------------------------+


Outputs
=======

+--------------------+---------------------------+-------------------------------------------------------------------------------+
| Output Name        | Description               | Sample Value                                                                  |
+====================+===========================+===============================================================================+
| BucketArn          | ARN of Bucket             | arn:aws:s3:::xyz-core-automation-ap-southeast-1                               |
+--------------------+---------------------------+-------------------------------------------------------------------------------+
| BucketName         | Bucket Name               | xyz-core-automation-ap-southeast-1                                            |
+--------------------+---------------------------+-------------------------------------------------------------------------------+
| Build              | Build number              | 1                                                                             |
+--------------------+---------------------------+-------------------------------------------------------------------------------+
| Prefix             | S3 Prefix                 | files/branch/demo/canary/testing/logs                                         |
+--------------------+---------------------------+-------------------------------------------------------------------------------+
| S3Url              | S3 endpoint URL           | s3://xyz-core-automation-ap-southeast-1/files/branch/demo/canary/testing/logs |
+--------------------+---------------------------+-------------------------------------------------------------------------------+
| S3UrlDeploymentDns | DNS name of S3 Deployment | s3-logs.testing-1.canary.demo.sin.auto.nonprod.c0.xyz.com                     |
+--------------------+---------------------------+-------------------------------------------------------------------------------+
