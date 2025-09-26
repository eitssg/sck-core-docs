===============
Getting Started
===============

Requirements
============

To test core-automation, checkout both ``core-automation`` and ``demo-bluegreen`` (or ``demo-canary``) next to each other.

You need ``~/.aws/credentials`` configured with a suitable profile (e.g. ``abc-automation``).

You need python3 and pip3.

Setup python
============

``pip3 install awscli boto3 sphinx sphinx_rtd_theme``

.. todo::

	use pipenv?

Setup your editor
=================

Most of us use SublimeText. VSCode is a good, free alternative.

PEP8
----

We follow PEP8, but only where it makes sense.

If using SublimeText, install Anaconda then edit user settings:

.. code-block:: json

	{
	    "anaconda_linter_mark_style": "stippled_underline",
	    "anaconda_gutter_marks": false,
	    "pep8_max_line_length": 999,
	    "pep8_ignore": [
	       "_E302",
	       "E402"
	   ]
	}

Restructured Text (RST) Snippets
--------------------------------

Install this. Lots of handy SublimeText hotkeys for working with RST - in particular, see `magic tables <https://github.com/mgaitan/sublime-rst-completion#magic-tables>`_

Installing Python 3.x on OSX
============================

Use the latest python.org package for installation of python3.x.

Do not install python3 via brew. Brew has a bug in distutils which will make installation of core-automation lambda dependencies difficult. 
If you have already installed python3 via brew, the recommended action is to uninstall correctly and reinstall via the offical python.org package.

https://www.python.org/downloads/

It is not recommended to symlink 'python' to python3 binaries as this will cause problems with osx/other software. 
Instead, call python3 directly when you want to use it.

e.g.

.. code-block:: bash

    python script_in_python2.py
    python3 script_in_python3.py

You may want to link pip to pip3 if you are working exclusively in python3.x. 

Update git if using OSX
=========================

OSX by default ships with a version of git which is quite old and missing features and fixes.
You can validate this with the following

.. code-block:: bash

	/usr/bin/git --version 

The result should be something similar to: git version 2.13.5 (Apple Git-94)

You should upgrade git using brew. This will help you with a number of git issues including the credential helper issue.

.. code-block:: bash

	brew info git
	brew install git 
	brew link git
	/usr/bin/git --version 

The output should display a git version equal to or greater than 2.20.x (as of Feb 2019)

Setup Bash 4 if using OSX
=========================

Otherwise associative arrays do not work

.. code-block:: bash

    brew install bash
    #Set default shell for your user
    echo /usr/local/bin/bash >> /etc/shells
    chsh -s /usr/local/bin/bash
    #Optional set bash4 for root user also
	sudo -s
	echo /usr/local/bin/bash >> /etc/shells
	chsh -s /usr/local/bin/bash


Setup core-automation
=====================

.. code-block:: bash

    cd core-automation
    python3 bin/install-lambda-dependencies.py


Updating jinja2 filters without pip
===================================

Can skip pip step and only copy common files:

``python3 bin/install-lambda-dependencies.py common``

(useful if you're tweaking the filters)

Test deploying demo-canary
===========================

See :doc:`deploying_apps` for instructions on simulating the pipeline locally.