===============================
Simple Cloud Kit Documentation
===============================

Welcome to the comprehensive documentation library for Simple Cloud Kit (SCK) Core - a powerful automation framework for AWS cloud deployments. Whether you're just getting started or looking for detailed technical references, you'll find everything you need here.

.. raw:: html

   <div style="margin: 2rem 0; padding: 2rem; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; border-radius: 8px; text-align: center;">
     <h2 style="margin: 0 0 1rem 0; color: white;">🚀 Simple Cloud Kit Core</h2>
     <p style="margin: 0; font-size: 1.1em; opacity: 0.9;">Multi-tenant AWS automation platform with deployment pipelines, infrastructure as code, and comprehensive audit trails.</p>
   </div>

📚 Documentation Sections
==========================

CI/CD User Guide - Get Started
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Perfect for newcomers and end users who want to learn how to deploy infrastructure using SCK Core.

.. raw:: html

   <div style="margin: 1rem 0; padding: 1.5rem; border-left: 4px solid #28a745; background: #f8f9fa;">
     <h4 style="margin: 0 0 1rem 0;">🎯 <a href="/docs/user_guide/" style="color: #28a745; text-decoration: none;">CI/CD User Guide</a></h4>
     <ul style="margin: 0;">
       <li><a href="/docs/user_guide/getting-started.html">Getting Started & Installation</a></li>
       <li><a href="/docs/user_guide/introduction.html">Platform Introduction</a></li>
       <li><a href="/docs/user_guide/directory-structure.html">Project Directory Structure</a></li>
       <li><a href="/docs/user_guide/describing-your-infrastructure.html">Infrastructure as Code</a></li>
       <li><a href="/docs/user_guide/useful-patterns.html">Deployment Patterns & Best Practices</a></li>
       <li><a href="/docs/user_guide/consumables.html">Consumables & Components</a></li>
       <li><a href="/docs/user_guide/pipeline-functions.html">Pipeline Functions</a></li>
       <li><a href="/docs/user_guide/kms-keys.html">KMS Key Management</a></li>
       <li><a href="/docs/user_guide/teardown-protection.html">Teardown Protection</a></li>
     </ul>
   </div>

Technical Reference - API Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Comprehensive API documentation for developers working with SCK Core modules and architecture.

.. raw:: html

   <div style="margin: 1rem 0; padding: 1.5rem; border-left: 4px solid #007bff; background: #f8f9fa;">
     <h4 style="margin: 0 0 1rem 0;">🔧 <a href="/docs/technical_reference/" style="color: #007bff; text-decoration: none;">Technical Reference</a></h4>
     <ul style="margin: 0;">
       <li><a href="/docs/technical_reference/introduction.html">Architecture Overview</a></li>
       <li><a href="/docs/technical_reference/modules.html">Complete Module Index</a></li>
       <li><strong>Foundation Layer:</strong></li>
       <ul>
         <li><a href="/docs/technical_reference/core-framework/core-framework.html">Core Framework - Models & Utilities</a></li>
         <li><a href="/docs/technical_reference/core-helper/core-helper.html">Core Helper - AWS Integration</a></li>
         <li><a href="/docs/technical_reference/core-logging/core-logging.html">Core Logging - Structured Logging</a></li>
         <li><a href="/docs/technical_reference/core-renderer/core-renderer.html">Core Renderer - Template Processing</a></li>
       </ul>
       <li><strong>Data Layer:</strong></li>
       <ul>
         <li><a href="/docs/technical_reference/core-db/core-db.html">Database Layer - DynamoDB Operations</a></li>
       </ul>
       <li><strong>Execution Layer:</strong></li>
       <ul>
         <li><a href="/docs/technical_reference/core-execute/core-execute.html">Execution Engine - Step Functions</a></li>
         <li><a href="/docs/technical_reference/core-runner/core-runner.html">Core Runner - Execution Orchestration</a></li>
         <li><a href="/docs/technical_reference/core-report/core-report.html">Core Report - Status Reporting</a></li>
       </ul>
       <li><strong>Compilation Layer:</strong></li>
       <ul>
         <li><a href="/docs/technical_reference/core-deployspec-compiler/core-deployspec-compiler.html">Deployment Spec Compiler</a></li>
         <li><a href="/docs/technical_reference/core-component-compiler/core-component-compiler.html">Component Compiler</a></li>
       </ul>
       <li><strong>Service Layer:</strong></li>
       <ul>
         <li><a href="/docs/technical_reference/core-invoker/core-invoker.html">Lambda Orchestration</a></li>
         <li><a href="/docs/technical_reference/core-api/core-api.html">REST API - FastAPI Endpoints</a></li>
         <li><a href="/docs/technical_reference/core-organization/core-organization.html">Organization Management</a></li>
       </ul>
     </ul>
   </div>

Developer Guide - Contributing & Development
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Resources for developers who want to contribute to or extend SCK Core platform.

.. raw:: html

   <div style="margin: 1rem 0; padding: 1.5rem; border-left: 4px solid #6f42c1; background: #f8f9fa;">
     <h4 style="margin: 0 0 1rem 0;">👨‍💻 <a href="/docs/developer_guide/" style="color: #6f42c1; text-decoration: none;">Developer Guide</a></h4>
     <ul style="margin: 0;">
       <li><a href="/docs/developer_guide/setup.html">Development Environment Setup</a></li>
       <li><a href="/docs/developer_guide/api_reference.html">API Development Guidelines</a></li>
       <li><a href="/docs/developer_guide/modules.html">Module Architecture Overview</a></li>
       <li><strong>Coming Soon:</strong></li>
       <ul>
         <li><em>Testing Guidelines & Best Practices</em></li>
         <li><em>Code Style & Contribution Standards</em></li>
         <li><em>Docker Development Environment</em></li>
         <li><em>CI/CD Pipeline Integration</em></li>
         <li><em>Creating Custom Consumables</em></li>
         <li><em>Extending Pipeline Functions</em></li>
       </ul>
     </ul>
   </div>

🎯 Quick Start Recommendations
===============================

New to SCK Core? Follow this learning path:

1. **📖 Read the Introduction** - `Platform Overview </docs/user_guide/introduction.html>`_
2. **🚀 Installation Guide** - `Getting Started </docs/user_guide/getting-started.html>`_
3. **🏗️ Project Structure** - `Directory Structure </docs/user_guide/directory-structure.html>`_
4. **📋 Infrastructure as Code** - `Describing Your Infrastructure </docs/user_guide/describing-your-infrastructure.html>`_
5. **🔍 Architecture Deep Dive** - `Technical Reference </docs/technical_reference/>`_

Need Help?
==========

.. raw:: html

   <div style="margin: 2rem 0; padding: 1.5rem; background: #fff3cd; border: 1px solid #ffeaa7; border-radius: 4px;">
     <h4 style="margin: 0 0 1rem 0;">💡 Support Resources</h4>
     <ul style="margin: 0;">
       <li>📋 <a href="/docs/user_guide/useful-patterns.html">Deployment Patterns & Best Practices</a></li>
       <li>🔧 <a href="/docs/user_guide/teardown-protection.html">Teardown Protection Guidelines</a></li>
       <li>🔑 <a href="/docs/user_guide/kms-keys.html">KMS Key Management</a></li>
       <li>🐛 <strong>Issues:</strong> GitHub repository issues section</li>
       <li>📚 <strong>Examples:</strong> See consumables and pipeline functions</li>
     </ul>
   </div>