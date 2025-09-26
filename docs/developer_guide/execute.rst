============
Core Execute
============

The core_execute Lambda is the main component of the action runner. It is responsible for executing a list of actions. It performs the following tasks:

* Download list of actions from S3
* Download state from S3
* Check status of any executing actions
* Execute any runnable actions
* Upload updated state to S3
* Instruct the orchestrating system (Step Functions) of the next state to transition into (wait, execute, success, failure), through use of the `flow_control` output variable

See also :doc:`actions`.

core_execute
============

.. automodule:: core_execute
    :members:
    :undoc-members:

actionlib
=========

.. automodule:: core_execute.actionlib
    :members:
    :undoc-members:


actionlib.action
----------------

.. automodule:: core_execute.actionlib.action
    :members:
    :undoc-members:

actionlib.factory
-----------------

.. automodule:: core_execute.actionlib.factory
    :members:
    :undoc-members:

actionlib.helper
----------------

.. automodule:: core_execute.actionlib.helper
    :members:
    :undoc-members:



