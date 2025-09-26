===================
Deployspec Compiler
===================

main
====

.. automodule:: deployspec_compiler.main
    :members:
    :undoc-members:


Validation
==========

Basic validation exists to prevent duplicate ``stack_name`` values in the deployspec.yaml file. Uniqueness is enforced for ``account/region/stack_name``:

.. code-block:: bash

	{"Timestamp": "2019-01-21 03:49:54.318259", "Type": "STATUS", "Status": "COMPILE_FAILED", "Reason": "Deployspec compilation failed", "Details": {"Scope": "deployspec"}, "Resource": "prn:demo:stackclash:master:1"}
	Traceback (most recent call last):
	  File "./cli.py", line 99, in <module>
	    run(args)
	  File "./cli.py", line 92, in run
	    response = lambda_function.handler(event, {})
	  File "/path/to/core-automation/lambdas/deployspec_compiler/main.py", line 74, in handler
	    validate_deployspec(deployspec)
	  File "/path/to/core-automation/lambdas/deployspec_compiler/main.py", line 187, in validate_deployspec
	    raise ValueError('Found duplicate stack_names={}'.format(dupes))
	ValueError: Found duplicate stack_names=[{'count': 2, 'stack_name': '831054035051/ap-southeast-1/{{ core.Project }}-{{ core.App }}-test1'}, {'count': 2, 'stack_name': '335723636949/ap-southeast-1/{{ core.Project }}-{{ core.App }}-test1'}]

.. note::
	When we find the first exception to this rule, we'll add a flag to bypass the validation step for that stack_name.
