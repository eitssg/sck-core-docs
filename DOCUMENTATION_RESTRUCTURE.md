# SCK Core Documentation - Modernization Recommendations

## Current Issues Analysis

### Import Errors Fixed:
1. ✅ `core_framework.magic` → `core_helper.magic` 
2. ✅ `core_renderer.monkeypatch` → `core_renderer.filters` (monkeypatch doesn't exist)
3. ✅ Removed outdated `_autosummary` directories

### Remaining Issues to Address:
1. `core_framework.models.actions.*` - These don't exist as modules, only as individual files
2. `core_api.api.auth_handler` - Should reference actual auth modules
3. `core_api.types`, `core_api.handler_*` - These modules don't exist

## Recommended Documentation Structure

### Problem with Current Structure:
- **Too technical-first**: Starts with low-level API documentation
- **Poor discoverability**: Users can't find what they need
- **Outdated references**: Many broken links and imports
- **No clear user journey**: No obvious path from beginner to advanced

### Proposed New Structure:

```
docs/
├── library/                               # Home page for all docs.  Will be publish at url http://<server>/docs
│   ├── index.rst                           
├── getting-started/                       # Quick start guides
│   ├── index.rst
│   ├── installation.rst
│   ├── quickstart.rst
│   └── first-deployment.rst
├── user-guides/                          # Task-oriented guides  
│   ├── index.rst
│   ├── portfolio-management.rst
│   ├── deployment-workflows.rst
│   ├── organization-setup.rst
│   └── troubleshooting.rst
├── concepts/                             # Understanding the system
│   ├── index.rst
│   ├── architecture-overview.rst
│   ├── portfolio-model.rst
│   ├── multi-tenant-model.rst
│   ├── deployment-lifecycle.rst
│   └── security-model.rst
├── tutorials/                            # Step-by-step examples
│   ├── index.rst
│   ├── basic-portfolio-setup.rst
│   ├── custom-actions.rst
│   └── advanced-deployment.rst
├── reference/                            # API and module documentation
│   ├── index.rst
│   ├── api/                             # REST API docs
│   ├── modules/                         # Python module docs
│   │   ├── core-framework/
│   │   ├── core-api/
│   │   ├── core-db/
│   │   └── ...
│   └── cli/                            # Command line reference
└── development/                         # For contributors
    ├── index.rst
    ├── setup.rst
    ├── contributing.rst
    ├── testing.rst
    └── architecture.rst
```

### Benefits of New Structure:
1. **User-centric**: Starts with what users want to accomplish
2. **Progressive disclosure**: Basic → intermediate → advanced → reference
3. **Task-oriented**: Organized around user goals, not code structure
4. **Modern documentation patterns**: Follows Diátaxis methodology
5. **Better SEO and navigation**: Clear hierarchy and cross-references

## Implementation Steps:

### Phase 1: Fix Immediate Issues (Now)
- ✅ Fix broken module imports
- ✅ Clean up autosummary artifacts
- Update conf.py to ignore missing modules
- Test build succeeds

### Phase 2: Content Audit (Next)
- Review existing content for accuracy
- Identify gaps in user-facing documentation
- Map current content to new structure

### Phase 3: Restructure (Future)
- Implement new directory structure
- Migrate and improve existing content
- Add missing user guides and tutorials
- Improve navigation and cross-references

### Phase 4: Modernize (Future)
- Add OpenAPI specs for REST APIs
- Interactive examples and code samples
- Better visual design and branding
- Search improvements

## Immediate Actions Needed:

1. **Update conf.py** to handle missing modules gracefully
2. **Create user-focused landing page** instead of technical reference first
3. **Add practical examples** showing real-world usage
4. **Improve navigation** with better toctree organization
5. **Add search and discovery** features