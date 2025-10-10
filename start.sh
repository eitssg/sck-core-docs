#!/usr/bin/env bash

# Start the Core Docs server in production mode

echo "Starting Core Docs server in production mode..."
echo "Server will be available at: http://localhost:8100"
echo "Documentation will be served at: http://localhost:8100/docs"
echo ""

# Production mode with Uvicorn (Windows-compatible)
uvicorn core_docs.server:app \
    --host 0.0.0.0 \
    --port 8100 \
    --log-level info \
    --no-use-colors \
    --access-log
