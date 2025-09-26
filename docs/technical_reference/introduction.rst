.. _technical-reference-introduction:

============
Introduction
============

Core Automation Platform
=========================

A completely opinionated and obnoxiously correct, even if in its own mind, model for forcing a behaviour in AWS.

The Core Automation Platform is a comprehensive infrastructure-as-code system designed to manage AWS resources at scale. It provides a layered architecture where each component has a specific responsibility in the deployment and management lifecycle.

Architecture Overview
=====================

The platform is built as a 16-layer architecture, each serving a specific purpose in the automation pipeline:

Layer 1 - Foundation Components
-------------------------------

**Core Framework**
   The foundational models that provide tools and structures used by all layers. Standard YAML and JSON extensions.

**Core Helper**
   Tools that provide convenience functions for interacting with AWS or Local system.

**Core Logging**
   An enhanced python logging facility that provides easier interoperability between CloudWatch Logging and local Logging. Includes trace level logging capabilities.

**Core Renderer**
   Jinja2 Rendering enhancements with custom filters and round-trip rendering capabilities.

Layer 2 - Data Management
-------------------------

**Core DB**
   The database integration system using PynamoDB on DynamoDB. This is where all the CMDB is managed, storing events (such as deployments) and items (Components) created and deployed for applications.

Layer 3 - Execution Engine
--------------------------

**Core Execute**
   Manages CloudFormation stacks and performs standard actions on AWS including granting privileges, copying images to other accounts, user management, and stack lifecycle operations (plan, apply, deploy, teardown). Runs as an AWS Step-Function to process lists of actions.

Layer 4 - Reporting
-------------------

**Core Report**
   Handles logging and reporting of task outcomes. Provides execution status and audit trails for all automation activities.

Layer 5 - Task Orchestration
----------------------------

**Core Runner**
   Takes task payloads, generates unique execution IDs (correlation IDs), logs tasks to the database, and initiates Core Execute step-functions. Acts as the primary task dispatcher.

Layer 6 - Multi-Account Deployment
----------------------------------

**Core Deployspec**
   Expands simple action lists to run across multiple AWS accounts and regions. Takes actions designed for single account/region and creates distributed execution plans for hundreds of accounts simultaneously.

Layer 7 - Infrastructure Generation
-----------------------------------

**Core Component**
   CloudFormation stack generator and actions generator. Compiles high-level component definitions into CloudFormation templates with proper tagging and security configurations. Acts as the Component Compiler.

Layer 8 - Traffic Management
----------------------------

**Core Invoker**
   The traffic cop of the system. Receives tasks and routes them to appropriate processors (DeploySpec, Component, or direct Runner execution). Provides a unified interface for all task execution.

Layer 9 - Account Management
----------------------------

**Core Organization**
   Manages AWS Organizations, OUs, and account creation. Provides account factory capabilities with proper role setup for automation system access.

Layer 10 - Source Integration
-----------------------------

**Core Codecommit**
   AWS CodeCommit integration trigger. Monitors infrastructure repositories for changes in /platform folders and automatically initiates deployment workflows.

Layer 11 - API Interface
------------------------

**Core API**
   JSON HTTP API supporting both FastAPI (containerized) and AWS API Gateway deployment modes. Provides programmatic access to all automation capabilities.

Layer 12 - Command Line Interface
---------------------------------

**Core CLI**
   Command-line wrapper for task composition and execution. Handles artifact upload to S3 and integrates with CI/CD platforms (GitHub, GitLab, Bamboo, CircleCI, ArgoCD).

Layer 13 - User Interface
-------------------------

**Core UI**
   Web-based dashboard for infrastructure visualization and management. Provides account creation, portfolio management, deployment monitoring, and comprehensive infrastructure visibility.

Supporting Components
=====================

**Core Docs (Layer 14)**
   Complete user and reference documentation including template creation guides, action definitions, and AWS Landing Zone management at scale.

**Core Docker Base (Layer 15)**
   Golden image operating system foundation for containerized deployments. Provides stable, reusable base services.

**Core Docker (Layer 16)**
   Complete Core Automation Platform in a container. Supports deployment on Docker Desktop or Kubernetes with persistent volume requirements.

System Integration
==================

The layers work together in a coordinated fashion:

1. **Tasks** are submitted via CLI, API, or UI
2. **Core Invoker** routes tasks to appropriate processors
3. **Core Component/Deployspec** compile templates and actions
4. **Core Runner** orchestrates execution with unique correlation IDs
5. **Core Execute** performs actual AWS operations via Step Functions
6. **Core DB** maintains state and audit trails
7. **Core Report** provides execution feedback

This architecture ensures scalability, reliability, and comprehensive audit capabilities for enterprise AWS infrastructure management.

Module Reference
================

The following sections provide detailed API documentation for each core module:

.. toctree::
   :maxdepth: 2
   
   core-framework/core-framework
   core-db/core-db
   core-execute/core-execute
   core-report/core-report
   core-runner/core-runner
   core-deployspec-compiler/core-deployspec-compiler
   core-component-compiler/core-component-compiler
   core-invoker/core-invoker
   core-organization/core-organization
   core-api/core-api