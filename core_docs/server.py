import fastapi
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pathlib import Path

app = fastapi.FastAPI(
    title="Core Docs", 
    version="0.1.0",
    docs_url=None,  # Disable /docs
    redoc_url=None  # Disable /redoc
)

# Mount static files for serving documentation
docs_path = Path(__file__).parent.parent / "build"
if docs_path.exists():
    app.mount("/docs", StaticFiles(directory=str(docs_path), html=True), name="docs")

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs", status_code=302)