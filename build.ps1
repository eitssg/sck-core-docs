param (
    [string[]]$docLibs = @("developer_guide", "technical_reference", "user_guide", "library")
)

if ($docLibs -contains "all") {

    poetry build

    Remove-Item -Recurse -Force "build" -ErrorAction SilentlyContinue
    New-Item -ItemType Directory -Path "build" -ErrorAction SilentlyContinue | Out-Null
}

if ($docLibs -contains "developer_guide" -or $docLibs -contains "all") {
    Write-Host "Building Developer Guide..." -ForegroundColor Green
    Remove-Item -Recurse -Force "build/developer_guide" -ErrorAction SilentlyContinue
    sphinx-build -b html docs/developer_guide build/developer_guide
}

if ($docLibs -contains "technical_reference" -or $docLibs -contains "all") {
    Write-Host "Building Technical Reference..." -ForegroundColor Green
    Remove-Item -Recurse -Force "build/technical_reference" -ErrorAction SilentlyContinue
    sphinx-build -b html docs/technical_reference build/technical_reference
}

if ($docLibs -contains "user_guide" -or $docLibs -contains "all") {
    Write-Host "Building User Guide..." -ForegroundColor Green
    Remove-Item -Recurse -Force "build/user_guide" -ErrorAction SilentlyContinue
    sphinx-build -b html docs/user_guide build/user_guide
}

if ($docLibs -contains "library" -or $docLibs -contains "all") {
    Write-Host "Building Library Documentation..." -ForegroundColor Green
    Remove-Item -Recurse -Force "build/library" -ErrorAction SilentlyContinue
    sphinx-build -b html docs/library build
}
