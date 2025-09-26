================
AWS::S3::Bucket
================

Architectural Outcome
=====================

The consumable creates an S3 bucket for use by the application. The bucket uses default server-side encryption with AWS KMS-managed Keys (SSE-KMS).

The resource is configured according to properties and default set out below.

Quick Start
===========

.. literalinclude:: ../samples/s3-bucket-quickstart.yaml
  :language: yaml
  :caption: AWS::S3::Bucket Quick Start

Resources
=========

S3 Bucket
---------

:Naming pattern: ``Bucket``
:Required: Yes
:Reference: `AWS::S3::Bucket <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket.html>`_

.. table:: Available Properties
    :widths: grid

    +-------------------------+------------------------------+----------------------------------------------------------------------+
    | Property                | Default Value                | Comments                                                             |
    +=========================+==============================+======================================================================+
    | BucketName              | Optional, default is 'build' | Value must use the Fn::Pipeline::S3BucketName function               |
    +-------------------------+------------------------------+----------------------------------------------------------------------+
    | LifecycleConfiguration  | Optional                     | Supports lifecyle events based on AbortIncompleteMultipartUpload     |
    |                         |                              | ExpirationDate, ExpirationInDays, NoncurrentVersionExpirationInDays, |
    |                         |                              | Prefix                                                               |
    +-------------------------+------------------------------+----------------------------------------------------------------------+
    | VersioningConfiguration | Optional, default is omitted | Allowed values: Enabled and Suspended. The default is Suspended.     |
    +-------------------------+------------------------------+----------------------------------------------------------------------+

Security
========

Encryption
----------

The S3 bucket is created with default KMS encryption and a policy to enforce this encryption.

See `Amazon S3 Default Encryption for S3 Buckets <https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html>`_.

Outputs
=======

+--------------------------+---------------------------------------------+-------------------------------------------------------------+
| Output Name              | Description                                 | Sample Value                                                |
+==========================+=============================================================+=============================================+
| BucketArn                | ARN of Bucket                               | arn:aws:s3:::demo-canary-testing-s3-bucket                  |
+--------------------------+---------------------------------------------+-------------------------------------------------------------+
| BucketName               | Name of the bucket                          | demo-canary-testing-s3-bucket                               |
+--------------------------+---------------------------------------------+-------------------------------------------------------------+
| Build                    | Build number                                | 1                                                           |
+--------------------------+---------------------------------------------+-------------------------------------------------------------+
| S3BucketUrl              | S3 endpoint URL                             | s3://demo-canary-testing-1-s3-bucket                        |
+--------------------------+---------------------------------------------+-------------------------------------------------------------+
| S3BucketUrlDeploymentDns | Deployment DNS record, CNAME to S3BucketUrl | s3-bucket.testing-1.canary.demo.sin.auto.nonprod.c0.xyz.com |
+--------------------------+---------------------------------------------+-------------------------------------------------------------+
