==============================
Repository directory structure
==============================

Applications deployed by the pipeline need to include the following directory structure in their source control repository::

    /
    ├── <other repository files>
    ├── platform
    |   ├── components
    |   |   └── <component definitions>
    |   ├── files
    |   |   └── <static files>
    |   ├── vars
    |   |   └── <var files>
    |   └── package.sh


* components - component definition YAML files
* files - files to be uploaded and made available to deployed resources
* vars - variables YAML files
* package.sh - copies files generated during CI to the /platform/files directory

Note that components can be named as desired, but the names should be kept fairly short where possible (<15 characters) since the component name is included in DNS names, and these DNS names have have a limited maximum length.

Components
==========
Please refer to:

  :ref:`Describing your infrastructure <components>`


Files
=====

Files placed in the files directory will be uploaded to S3 and will be accessible in the component spec.

.. _variables:

Variables
=========

The variables file is located in the vars directory in the platform folder.

We can use variables to set environment specific parameters based on branch name.  This is useful for parameters such as KeyName, MultiAZ, InstanceType and application specific configuration, such as connection strings, usernames, and passwords.

The vars.yaml file should be composed in the following format:

.. code-block:: yaml

    <branch name 1>:
      <key name 1>: <value 1>
      <key name 2>: <value 2>
      .
      .
      .
      <key name n>: <value 1>
    .
    .
    .
    <branch name n>:
      <key name 1>: <value 1>
      <key name 2>: <value 2>
      .
      .
      .
      <key name n>: <value 1>

For example, in the non-production branch, we can set the InstanceType for servers to be a lower, cheaper tier, such as a t3.micro, as performance may not be a critical factor in non-production.
For the production branch (master), we can set the InstanceType to meet the system requirements for the application, such as a m3.medium.  This will allow us to optimize development costs, as well as predicting the costs of development and production environments more accurately.

Defaults can be set in the variables file, such that those variables will be used if there is no matching branch name when you deploy your application.
For example, if you named a branch "JIRA-123", it would use the default variables, as the branch name does not match those defined in the variables file (i.e. uat, master)
As shown below, by using the keyword *_defaults* as the branch name, these variables will be used as the default variables if there is no matching branch name.

.. code-block:: yaml

    _defaults:
      KeyName: myapp
      InstanceType: t3.micro
      MultiAZ: false
    uat:
      KeyName: foobar
    master:
      KeyName: myapp-prod
      InstanceType: m3.medium
      MultiAZ: true

We can reference variables within our component spec using the following syntax:

.. code-block:: yaml

    {{ vars.<name of the variable }}

For example:

.. code-block:: yaml

    LaunchConfiguration:
      Properties:
        InstanceType: {{ vars.InstanceType }}
        KeyName: {{ vars.KeyName }}

The value that will be substituted will depend on the name of the branch - if no matching branch name is found, the _defaults values will be used.

package.sh
==========

The package.sh script will be called to upload specified files in the repository to S3.  Files can be referenced in the component spec using the *Fn::Pipeline::FileUrl* pipeline function.

Example package.sh script:

.. code-block:: shell

    #!/bin/bash

    echo "package.sh start, REPO_DIR=${REPO_DIR}, FILES_DIR=${FILES_DIR}"

    mkdir -p $FILES_DIR
    cp -pr $REPO_DIR/src/* $FILES_DIR/

    echo "package.sh finish."

Please refer to:

  :ref:`pipeline-functions`
