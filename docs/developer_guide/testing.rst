=======
Testing
=======

.. todo::

	Write notes on how to test the pipe.


Core Automation Unit Tests
==========================

From your laptop:

.. code-block:: bash

	# need pipenv to run with a consistent environment.
	pip install pipenv

	# Use the --python arg if you're getting: OSError: [Errno 8] Exec format error: '/mnt/c/Users/YourUserName/AppData/Local/Microsoft/WindowsApps/python.exe'
	pipenv --python=/usr/bin/python3 install

	# wait a while...

	# See bitbucket-pipelines.yml for the latest example that's automated
	pipenv run py.test -vv \
	--cov=apihelper --cov=awshelper --cov=filters --cov=log --cov=util \
	--cov-report term-missing \
	--cov-report xml:test-reports/coverage.xml --junitxml=test-reports/unittest.xml \
	--cov-report html:unittest-report \
	tests/


Compiling Apps Locally
======================

To test pipeline changes, the compiler lambda has been uplifted to support better CLI options, and an ability to run in "local" mode, which does not upload compiled files into S3, instead depositing them into ``app-path/_compiled``.

.. code-block:: bash

	component_compiler$ python3 cli.py -h
	usage: cli.py [-h] [--mode MODE] [--aws-profile AWS_PROFILE]
	              [--app-path APP_PATH] [--bucket-region BUCKET_REGION]
	              [--bucket-name BUCKET_NAME]
	              portfolio app branch build

	Component Compiler for the Action Runner

	positional arguments:
	  portfolio             Portfolio name
	  app                   Application name
	  branch                Branch name (with dashes instead of underscores)
	  build                 Build number

	optional arguments:
	  -h, --help            show this help message and exit
	  --mode MODE           Mode of operation (None|test|local) (default: None)
	  --aws-profile AWS_PROFILE
	                        Select which profile to use from your
	                        ~/.aws/credentials file. (default: None)
	  --app-path APP_PATH   Local app path (local mode only) (default: None)
	  --bucket-region BUCKET_REGION
	                        S3 Bucket Region (default: ap-southeast-1)
	  --bucket-name BUCKET_NAME
	                        S3 Bucket Name (default: $client-core-automation-ap-
	                        southeast-1)


An example command would look like this:

.. code-block:: bash

	# Local mode
	python3 cli.py demo simpleapp staging 1 --mode=local --app-path=../../../demo-simpleapp

	# Test mode
	python3 cli.py demo simpleapp staging 1 --mode=test --aws-profile=core-automation-test --bucket-name=sourced-dev-island-core-automation-ap-southeast-1