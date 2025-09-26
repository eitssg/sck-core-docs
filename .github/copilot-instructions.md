# Copilot Instructions (Submodule: sck-core-docs)

- Tech: Sphinx documentation (Python-driven).
- Precedence: Local first; then root `../../.github/...`.
- Conventions: Keep docs consistent with UI/Backend contracts where referenced. Prefer reStructuredText for technical references, link to UI docs when UI behavior is discussed.

## CRITICAL - Python Environment Activation

**MANDATORY**: Before running ANY Python commands (including `python core_docs/build.py`, `.\build.ps1`, or Sphinx commands), you MUST activate the Poetry environment:

1. **Check Poetry environment path**:
   ```powershell
   poetry env info --path
   ```

2. **Activate the environment**:
   ```powershell
   & "PATH_FROM_ABOVE\Scripts\Activate.ps1"
   ```
   
3. **Then run Python commands**:
   ```powershell
   .\build.ps1 MODULE_NAME # e.g., user_guide, technical_reference, developer_guide, library, all  
   ```

**Never run Python commands without first activating the environment**. VSCode may not auto-activate when using centralized `.venvs` locations.

## ✅ IMPLEMENTED - Multi-Documentation Architecture

**CURRENT STATE**: Multi-manual documentation system with independent builds and professional landing page.

### ✅ Build System Architecture (IMPLEMENTED)
- **Build Script**: `build.ps1` - builds four independent documentation manuals
- **Server**: FastAPI server with static file serving at `/docs`
- **Landing Page**: Professional library index with navigation to all manuals

### ✅ Current Structure (IMPLEMENTED):
```
docs/
├── library/             # Landing page and navigation hub
├── user_guide/          # End-user documentation and tutorials
├── developer_guide/     # Contributing and development guidelines  
├── technical_reference/ # API documentation and module references

build/                   # Generated output
├── index.html           # Library landing page
├── user_guide/          # User manual HTML
├── technical_reference/ # API reference HTML  
└── developer_guide/     # Developer manual HTML
```

### ✅ Server Architecture (IMPLEMENTED):
- **FastAPI**: `core_docs/server.py` with OpenAPI docs disabled
- **Static Serving**: `/docs` serves from `build/` directory
- **Root Redirect**: `/` redirects to `/docs` 
- **Production**: Uvicorn server via `start.ps1`

### Technical Reference Guide

- **core_framework**
  - Docs Location: docs/technical-reference/core-framework
  - Source: docstrings in `core_framework` module
  - Project Dependency: None
- **core_logging**
  - Docs Location: docs/technical-reference/core-logging
  - Source: docstrings in `core_logging` module
  - Project Dependency: core_framework
- **core_helper**
  - Docs Location: docs/technical-reference/core-helper
  - Source: docstrings in `core_helper` module
  - Project Dependency: core_framework
- **core_renderer**
  - Docs Location: docs/technical-reference/core-renderer
  - Source: docstrings in `core_renderer` module
  - Project Dependency: core_framework
- **core_db**
  - Docs Location: docs/technical-reference/core-db
  - Source: docstrings in `core_db` module
  - Project Dependency: core_framework, core_logging
- **core_execute**
  - Docs Location: docs/technical-reference/core-execute
  - Source: docstrings in `core_execute` module
  - Project Dependency: core_framework, core_logging, core_db
- **core_report**
  - Docs Location: docs/technical-reference/core-report
  - Source: docstrings in `core_report` module
  - Project Dependency: core_framework, core_logging, core_db
- **core_runner**
  - Docs Location: docs/technical-reference/core-runner
  - Source: docstrings in `core_runner` module
  - Project Dependency: core_framework, core_logging, core_db, core_execute
- **core_deployspec**
  - Docs Location: docs/technical-reference/core-deployspec
  - Source: docstrings in `core_deployspec` module
  - Project Dependency: core_framework, core_logging, core_renderer, core_helper
- **core_component**
  - Docs Location: docs/technical-reference/core-component
  - Source: docstrings in `core_component` module
  - Project Dependency: core_framework, core_logging, core_renderer, core_helper
- **core_invoker**
  - Docs Location: docs/technical-reference/core-invoker
  - Source: docstrings in `core_invoker` module
  - Project Dependency: core_framework, core_db, core_deployspec, core_component, core_runner, core_helper
- **core_organization**
  - Docs Location: docs/technical-reference/core-organization
  - Source: docstrings in `core_organization` module
  - Project Dependency: core_framework, core_db, core_helper
- **core_api**
  - Docs Location: docs/technical-reference/core-api
  - Source: docstrings in `core_api` module
  - Project Dependency: core_framework, core_logging, core_db, core_invoker, core_helper, core_organization
- **core_codecommit**
  - Docs Location: docs/technical-reference/core-codecommit
  - Source: docstrings in `core_codecommit` module
  - Project Dependency: core_framework, core_logging, core_db, core_helper, core_invoker
- **core_cli**
  - Docs Location: docs/technical-reference/core-cli
  - Source: docstrings in `core_cli` module
  - Project Dependency: core_framework, core_logging, core_api

### Documentation Tree Rules
- **DO NOT** merge toctrees across documentation sets when implementing separate builds
- Each documentation set must remain completely independent with separate navigation
- Module import errors must be fixed by correcting references, not suppressing warnings

### Module Import Errors
- **DO NOT ignore missing modules** - these indicate incorrect references that must be fixed
- **DO NOT add `autodoc_mock_imports`** or `suppress_warnings` - breaking references must be corrected
- Module import errors indicate outdated documentation that needs correction, not suppression

## Contradiction Detection
- Ensure content aligns with UI/Backend contracts and root precedence.
- If conflict, warn + options + example.
- Example: "Doc suggests storing tokens in localStorage, which conflicts with UI auth docs; correct to session cookie/access token in memory."

## Standalone clone note
If cloned standalone, see:
- UI/backend conventions: https://github.com/eitssg/simple-cloud-kit/tree/develop/sck-core-ui/docs
- Root Copilot guidance: https://github.com/eitssg/simple-cloud-kit/blob/develop/.github/copilot-instructions.md
 
# WARNING

# Mulit-Tenancy

Reference multi-tenancy documentation in ./docs/multi-tenant.md for the most up-to-date information.  This documentation may be out of date.

## IMPORTANT - Documentation Status

**REQUIRED**: The sphinx documentation in this repo is NOT maintained. This documentation should be generated from docstrings in the code and from the UI documentation in sck-core-ui. Also, the users guide is from an old alpha version and is not up to date with the current codebase. Please DO NOT UNDER ANY CIRCUMSTANCES REFERENCE documentation in this repo for style, formatting, or code development. YOU MAY UPDATE THIS DOCUMENTATION AT WILL and fix it to 
match code, code style, docstring comments, and UI documentation in sck-core-ui.

**Source of Truth Priority**:
1. **CODE** - Always use current codebase as source of truth FIRST
2. **Docstrings** - Second priority for API documentation  
3. **Developer Confirmation** - Always confirm with developer regarding decisions from this documentation

## Multi-Tenancy Reference
Reference multi-tenancy documentation in `./docs/multi-tenant.md` for the most up-to-date information. This documentation may be out of date.