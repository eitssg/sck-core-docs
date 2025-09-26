
#!/usr/bin/env pwsh
# Start the Core Docs server in production mode

Write-Host "Starting Core Docs server in production mode..."
Write-Host "Server will be available at: http://localhost:8100"
Write-Host "Documentation will be served at: http://localhost:8100/docs"
Write-Host ""

# Production mode with Uvicorn (Windows-compatible)
uvicorn core_docs.server:app `
    --host 0.0.0.0 `
    --port 8100 `
    --log-level info `
    --no-use-colors `
    --access-log