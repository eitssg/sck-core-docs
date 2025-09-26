# SCK Core Documentation

Professional documentation system for Simple Cloud Kit (SCK) Core - a multi-tenant AWS automation framework.

## 📚 Documentation Structure

The documentation is organized into four independent manual sets:

- **Library** (`docs/library/`) - Main landing page and navigation hub
- **User Guide** (`docs/user_guide/`) - End-user documentation and tutorials  
- **Technical Reference** (`docs/technical_reference/`) - API documentation and module references
- **Developer Guide** (`docs/developer_guide/`) - Contributing and development guidelines

> **Copilot Note**: See [local instructions](.github/copilot-instructions.md) and [root guidance](../.github/copilot-instructions.md) for development precedence and module rules.

## 🏗️ Build System Architecture

### New Multi-Manual Build Process

The `build.ps1` script generates **independent documentation manuals** from RST source files:

```powershell
# Builds all documentation manuals
.\build.ps1

# Output structure:
build/
├── index.html              # Library landing page (from docs/library/)
├── user_guide/             # User manual (from docs/user_guide/)
├── technical_reference/    # API reference (from docs/technical_reference/)  
└── developer_guide/        # Developer manual (from docs/developer_guide/)
```

### Build Commands

```powershell
# Build all documentation manuals
.\build.ps1

# Start documentation server (serves at http://localhost:8100)  
.\start.ps1
```

### Server Architecture

The documentation is served via FastAPI with static file mounting:

- **Root (`/`)**: Redirects to `/docs`
- **Documentation (`/docs`)**: Serves built HTML from `build/` directory
- **Navigation**: Professional landing page with links to all manual sections

## 🚀 Quick Start

### Setup Environment

```powershell
# Clone repository (already done if you're reading this)
cd sck-core-docs

# Install dependencies (Poetry manages Python environment)
poetry install

# Activate virtual environment  
poetry shell
```

### Build & Serve Documentation  

```powershell
# Build all documentation
.\build.ps1

# Start documentation server
.\start.ps1

# Visit: http://localhost:8100
```

## 📖 Documentation Development

### Adding New Content

1. **User Guide**: Add RST files to `docs/user_guide/`
2. **Technical Reference**: Module docs auto-generated from docstrings  
3. **Developer Guide**: Add to `docs/developer_guide/`
4. **Main Library**: Update navigation in `docs/library/index.rst`

### RST Formatting Standards

- Use proper RST syntax with `::` for code blocks
- Include blank lines after `::` before code content  
- Use RST field lists: `:param name: description`
- Test with `.\build.ps1` to verify formatting

## 🔧 Architecture Details

### Independent Manual System

Each documentation section builds as a **separate Sphinx project**:

- Separate `conf.py` configuration for each manual
- Independent themes and styling
- Cross-manual linking via absolute URLs
- No shared toctree dependencies

### Static File Serving

FastAPI serves pre-built HTML files:
- No runtime documentation generation
- Fast serving of static assets
- Professional landing page with navigation
- Automatic index.html serving for directories
core-docs developer
```

Build both of them at the same time
```ps1
core-docs all
```

The users-guide and developer guid will be in the folder **`build`** in your current working folder

You can then navigate to the **`build\user-guide`** or **`build\developer-guide`** folder and run **`index.html`**

## Publishing to and S3 bucket

You may have infrastructure already deployed to share this documentation on a URL pointing to either an S3 bucket or CloudFront distribution.  (This script is for AWS, but feel free pubish on Azure or GCP as you desire)

Modify the publish.ps1 script to specify your folder

```ps1
# Buld all the documeentation
core-docs all

$USER_GUIDE_BUCKET = "core-automation-docs/user-guide"
$DEVELOPER_GUIDE_BUCKET = "core-automation-docs/developer-guide"

# Copy the contents of the build/user-guide directory to the S3 bucket
aws s3 cp build/user-guide/ s3://$USER_GUIDE_BUCKET/ --recursive

# Copy the contents of the build/developer-guide directory to the S3 bucket
aws s3 cp build/developer-guide/ s3://$DEVELOPER_GUIDE_BUCKET/ --recursive
```

The above script is in the file **`publish.ps1`** and can be easily executed on a build job in your CD pipeline (GitHub Actions or Bitbucket Pipeline)

An example of how to create the bucket is provided in the script **`create-bucket.psq`**

```text
Note:  We highly recommend you create in index.html page that will allow the users to choose
the developer guide or the user's guide and have that index.html file in your S3 bucket.  Make relevent
changes if you are going to have a different bucket for each guide and/or CloudFront origin paths
```
