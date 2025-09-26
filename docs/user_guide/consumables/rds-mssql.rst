===============
AWS::RDS::MSSQL
===============

Architectural Outcome
=====================

The component launches Managed database Resource based on MS SQL engine.  The resource is configured according to properties and default set out below.

.. image:: ../images/mssql.png
    :width: 75%
    :align: center

Quick Start
===========

.. literalinclude:: ../samples/rds-mssql-quickstart.yaml
  :language: yaml
  :caption: AWS::RDS::MSSQL Quick Start

Resources
=========

Database Instance
-----------------

:Naming pattern: ``DbInstance``
:Required: Yes
:Reference: `AWS::RDS::DBInstance <http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rds-database-instance.html>`_

.. table:: Available Properties
    :widths: grid

    +----------------------------+------------------+------------------------------------------------+
    | Property                   | Default Value    | Comments                                       |
    +============================+==================+================================================+
    | AllocatedStorage           |                  | Min 20 Gb, or 200 Gb for SE/EE                 |
    +----------------------------+------------------+------------------------------------------------+
    | AllowMajorVersionUpgrade   |                  |                                                |
    +----------------------------+------------------+------------------------------------------------+
    | AllowMinorVersionUpgrade   |                  |                                                |
    +----------------------------+------------------+------------------------------------------------+
    | BackupRetentionPeriod      | 7                |                                                |
    +----------------------------+------------------+------------------------------------------------+
    | CharacterSetName           |                  |                                                |
    +----------------------------+------------------+------------------------------------------------+
    | DBInstanceClass            |                  | Required                                       |
    +----------------------------+------------------+------------------------------------------------+
    | Engine                     |                  | Required                                       |
    +----------------------------+------------------+------------------------------------------------+
    | EngineVersion              |                  | If ommitted, AWS recommended version is used   |
    +----------------------------+------------------+------------------------------------------------+
    | LicenseModel               | license-included |                                                |
    +----------------------------+------------------+------------------------------------------------+
    | Iops                       |                  |                                                |
    +----------------------------+------------------+------------------------------------------------+
    | MasterUsername             |                  | Required                                       |
    +----------------------------+------------------+------------------------------------------------+
    | MasterUserPassword         |                  | Required                                       |
    +----------------------------+------------------+------------------------------------------------+
    | MonitoringInterval         | 60               | Set to 0 to disable enhanced monitoring        |
    +----------------------------+------------------+------------------------------------------------+
    | MultiAZ                    |                  |                                                |
    +----------------------------+------------------+------------------------------------------------+
    | PreferredBackupWindow      |                  | If omitted, AWS selects an out-of-hours window |
    +----------------------------+------------------+------------------------------------------------+
    | PreferredMaintenanceWindow |                  | If omitted, AWS selects an out-of-hours window |
    +----------------------------+------------------+------------------------------------------------+
    | Port                       | 1433             |                                                |
    +----------------------------+------------------+------------------------------------------------+
    | StorageType                | gp2              |                                                |
    +----------------------------+------------------+------------------------------------------------+
    | Timezone                   | UTC              |                                                |
    +----------------------------+------------------+------------------------------------------------+

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

Logging
=======

RDS for SQL Server does not support export to CloudWatch Logs. SQL Server database logs are available through the console, via the API or through use of stored procedure. See `Working with Microsoft SQL Server Logs <https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.Logs.html>`_.

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
| DbInstancePort     | DB Instance Port         | 1433         |
+--------------------+--------------------------+--------------+
| DeploymentDns      | DNS name of RDS Instance | <To do>      |
+--------------------+--------------------------+--------------+
