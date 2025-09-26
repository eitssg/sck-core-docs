===============
AWS::Image
===============

Architectural Outcomes
======================

This component does the following:

  1.  Launch an instance
  2.  Configure the instance:

      a.  Proxy setting
      b.  Deployment information setting
      c.  Extra packages manager install
      d.  aws-cfn-bootstrap (if base image is not Amazon Linux)
      e.  CloudWatch Log Agent

  3.  Create an AMI
  4.  Parallel actions:

      a.  Create an Encrypted AMI by copying the previously created AMI
      b.  Terminate the instance

  5.  Delete the unencrypted AMI


Quick Start
==================

Declare a ``AWS::Image`` Component to create a SOE Image. This example extends the instance configuration step to have more configurations with Ansible roles:

.. code-block:: yaml
    :caption: RHEL SOE quick start definition

    rhel:
      Type: AWS::Image
      Configuration:
        BakeInstance:
          Metadata:
            AWS::CloudFormation::Init:
              config:
                packages:
                  yum:
                    ansible: []
                sources:
                  /opt/pipeline:
                    Fn::Pipeline::FileUrl:
                      Path: "ansible/ansible.zip"
                commands:
                  00-run-ansible:
                    command: "ansible-playbook /opt/pipeline/ansible/ansible.yml -c local >> /var/log/cloud-init-output.log 2>&1"
          Properties:
            ImageId:
              Fn::Pipeline::ImageId:
                Name: rhel-7
            KeyName: sourced_group
            InstanceType: t3.micro

Resources
=========

Bake Instance
-------------

:Naming pattern: ``BakeInstance``
:Required: Yes
:Reference: `AWS::EC2::Instance <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html>`_

This resource is used to configure the instance used to bake the application AMI. The configuration of this resource should therefore include any required application bootstrap actions.

+----------------------+---------------+----------------------------------------------------+
| Available Properties | Default Value | Comments                                           |
+======================+===============+====================================================+
| ImageId              | <none>        | Value must use the Fn::Pipeline::ImageId function  |
+----------------------+---------------+----------------------------------------------------+
| InstanceType         | <none>        | Required                                           |
+----------------------+---------------+----------------------------------------------------+
| KeyName              | <none>        | Key must exist                                     |
+----------------------+---------------+----------------------------------------------------+

+---------------------------------------+---------------+----------+
| Available Top-Level Properties        | Default Value | Comments |
+=======================================+===============+==========+
| CreationPolicy.ResourceSignal.Timeout | PT15M         |          |
+---------------------------------------+---------------+----------+
| CreationPolicy.ResourceSignal.Count   | 1             |          |
+---------------------------------------+---------------+----------+
| Metadata                              | <none>        |          |
+---------------------------------------+---------------+----------+

Security
========

Security items
--------------

+------------------+-------------------------------------------------------------------------------+
| Name             | Description                                                                   |
+==================+===============================================================================+
| SecurityGroup    | The security group associated with the instance                               |
+------------------+-------------------------------------------------------------------------------+
| InstanceRole     | The instance role associated with the instance                                |
+------------------+-------------------------------------------------------------------------------+

Security Rules
--------------

+------------------+-------------------------------------------------------------------------------+
| Name             | Description                                                                   |
+==================+===============================================================================+
| SSH              | Allow SSH from bastion hosts                                                  |
+------------------+-------------------------------------------------------------------------------+


Outputs
=======

+--------------------------+--------------+----------------------------------------------------------------------------------+
| Output Name              | Sample Value |Description                                                                       |
+==========================+==============+==================================================================================+
| Build                    | 2            | Build number                                                                     |
+--------------------------+--------------+----------------------------------------------------------------------------------+
| DefaultExport            | <To do>      |                                                                                  |
+--------------------------+--------------+----------------------------------------------------------------------------------+
| InstanceId               | <To do>      | Instance Id of Bake Instance                                                     |
+--------------------------+--------------+----------------------------------------------------------------------------------+
| InstanceProfileArn       | <To do>      | Instance profile ARN                                                             |
+--------------------------+--------------+----------------------------------------------------------------------------------+
| InstanceProfileName      | <To do>      | Instance profile name                                                            |
+--------------------------+--------------+----------------------------------------------------------------------------------+
| SecurityGroupId          | <To do>      | Instance security group ID                                                       |
+--------------------------+--------------+----------------------------------------------------------------------------------+
| RoleArn                  | <To do>      | Role ARN                                                                         |
+--------------------------+--------------+----------------------------------------------------------------------------------+
| RoleName                 | <To do>      | Role Name                                                                        |
+--------------------------+--------------+----------------------------------------------------------------------------------+
