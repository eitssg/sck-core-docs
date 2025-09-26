====================
AWS::RDS::PostgreSQL
====================

Architectural Outcome
=====================

The component launches Managed database Resource based on PostgreSQL engine.  The resource is configured according to properties and default set out below.

.. image:: ../images/postgresql.png
    :width: 75%
    :align: center

Quick Start
===========

.. literalinclude:: ../samples/rds-postgresql-quickstart.yaml
  :language: yaml
  :caption: AWS::RDS::PostgreSQL Quick Start

Resources
=========

Database Instance
-----------------

:Naming pattern: ``DbInstance``
:Required: Yes
:Reference: `AWS::RDS::DBInstance <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html>`_

.. table:: Available Properties
    :widths: grid

    +----------------------------+---------------+------------------------------------------------+
    | Property                   | Default Value | Comments                                       |
    +============================+===============+================================================+
    | AllocatedStorage           |               | Required                                       |
    +----------------------------+---------------+------------------------------------------------+
    | AllowMajorVersionUpgrade   |               |                                                |
    +----------------------------+---------------+------------------------------------------------+
    | AllowMinorVersionUpgrade   |               |                                                |
    +----------------------------+---------------+------------------------------------------------+
    | BackupRetentionPeriod      | 7             |                                                |
    +----------------------------+---------------+------------------------------------------------+
    | CharacterSetName           |               |                                                |
    +----------------------------+---------------+------------------------------------------------+
    | DBInstanceClass            |               | Required                                       |
    +----------------------------+---------------+------------------------------------------------+
    | DBName                     |               |                                                |
    +----------------------------+---------------+------------------------------------------------+
    | EngineVersion              |               | If ommitted, AWS recommended version is used   |
    +----------------------------+---------------+------------------------------------------------+
    | Iops                       |               |                                                |
    +----------------------------+---------------+------------------------------------------------+
    | MasterUsername             |               | Required                                       |
    +----------------------------+---------------+------------------------------------------------+
    | MonitoringInterval         | 60            | Set to 0 to disable enhanced monitoring        |
    +----------------------------+---------------+------------------------------------------------+
    | MultiAZ                    |               |                                                |
    +----------------------------+---------------+------------------------------------------------+
    | PreferredBackupWindow      |               | If omitted, AWS selects an out-of-hours window |
    +----------------------------+---------------+------------------------------------------------+
    | PreferredMaintenanceWindow |               | If omitted, AWS selects an out-of-hours window |
    +----------------------------+---------------+------------------------------------------------+
    | StorageEncrypted           | true          |                                                |
    +----------------------------+---------------+------------------------------------------------+
    | StorageType                | gp2           |                                                |
    +----------------------------+---------------+------------------------------------------------+

Parameter Group
---------------

:Naming pattern: ``ParameterGroup``
:Required: No
:Reference: `AWS::RDS::DBParameterGroup <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-dbparametergroup.html>`_

.. table:: Available Properties
    :widths: grid

    +-------------+---------------+----------+
    | Property    | Default Value | Comments |
    +=============+===============+==========+
    | Description |               | Required |
    +-------------+---------------+----------+
    | Family      |               | Required |
    +-------------+---------------+----------+
    | Parameters  |               | Required |
    +-------------+---------------+----------+

Option Group
------------

:Naming pattern: ``OptionGroup``
:Required: No
:Reference: `AWS::RDS::OptionGroup <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-optiongroup.html>`_

.. table:: Available Properties
    :widths: grid

    +------------------------+---------------+----------+
    | Property               | Default Value | Comments |
    +========================+===============+==========+
    | EngineName             |               | Required |
    +------------------------+---------------+----------+
    | MajorEngineVersion     |               | Required |
    +------------------------+---------------+----------+
    | OptionGroupDescription |               | Required |
    +------------------------+---------------+----------+
    | OptionConfigurations   |               | Required |
    +------------------------+---------------+----------+

Security
========

Encryption
----------

All RDS instances are created with storage encryption enabled. This option cannot be changed.

See `Encrypting Amazon RDS Resources <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html>`_.

Outputs
=======

+--------------------+--------------------------+--------------+
| Output Name        | Description              | Sample Value |
+====================+==========================+==============+
| Build              | Build number             | 1            |
+--------------------+--------------------------+--------------+
| DbInstanceEndpoint | DB Instance Endpoint     | <To do>      |
+--------------------+--------------------------+--------------+
| DBInstanceId       | DB Instance Id           | <To do>      |
+--------------------+--------------------------+--------------+
| DbInstancePort     | DB Instance Port         | 3306         |
+--------------------+--------------------------+--------------+
| DeploymentDns      | DNS name of RDS Instance | <To do>      |
+--------------------+--------------------------+--------------+
