=============
Action Addons
=============

bake-image
----------

Used to provide an AMI bake step before deploying the resources stack.

Example use cases:

* Bootstrap an instance and create an AMI, used to launch auto-scaling group instances

Actions
=======

Deploy:

* Create bake security rules - "{{ context.ComponentPrn }}:action/deploy/main/bake-security-rules"
* Create bake instance - "{{ context.ComponentPrn }}:action/deploy/main/bake-instance"
* Create image - "{{ context.ComponentPrn }}:action/deploy/main/bake-image"
* Delete bake instance - "{{ context.ComponentPrn }}:action/deploy/main/delete-bake-instance"

Release:

* None

Teardown:

* Delete bake instance - "{{ context.ComponentPrn }}:action/teardown/main/bake-stack"
* Delete image - "{{ context.ComponentPrn }}:action/teardown/main/image"

Stacks
======

security-rules.yaml:

* Parameters:

    - KmsKeyArn
    - ResourcesStackName: ""
    - SecurityStackName
    - Stage: "bake"

bake.yaml:

* Parameters:

    - KmsKeyArn
    - SecurityStackName


build-instance
--------------

Used to create a temporary build stack before deploying the resources stack.

Example use cases:

* Perform Docker build and push before deploying resources

Actions
=======

Deploy:

* Create build security rules - "{{ context.ComponentPrn }}:action/deploy/main/build-security-rules"
* Create build instance - "{{ context.ComponentPrn }}:action/deploy/main/build-instance"
* Delete build instance - "{{ context.ComponentPrn }}:action/deploy/main/delete-build-instance"

Release:

* None

Teardown:

* Delete build instance - "{{ context.ComponentPrn }}:action/teardown/main/build-stack"

Stacks
======

security-rules.yaml:

* Parameters:

    - KmsKeyArn
    - ResourcesStackName: ""
    - SecurityStackName
    - Stage: "build"

build.yaml:

* Parameters:

    - KmsKeyArn
    - SecurityStackName

log-groups
----------

Used to create a log groups stack before deploying the resources stack.

Example use case:

* Creating log groups in a separate stack from resources allow the resources stack to fail and rollback while keeping the logs in tact for debugging
