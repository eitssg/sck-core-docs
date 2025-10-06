#!/usr/bin/env bash
set -euo pipefail

# Usage: ./build.sh [all|developer_guide technical_reference user_guide library]
# If no args are given, defaults to: developer_guide technical_reference user_guide library

docLibs=("$@")
if [[ ${#docLibs[@]} -eq 0 ]]; then
  docLibs=(developer_guide technical_reference user_guide library)
fi

contains() {
  local needle="$1"; shift
  for x in "$@"; do
    [[ "$x" == "$needle" ]] && return 0
  done
  return 1
}

if contains "all" "${docLibs[@]}"; then
  uv sync --all-extras
  uv build

  rm -rf build || true
  mkdir -p build
fi

if contains "developer_guide" "${docLibs[@]}" || contains "all" "${docLibs[@]}"; then
  echo "Building Developer Guide..."
  rm -rf build/developer_guide || true
  sphinx-build -b html docs/developer_guide build/developer_guide
fi

if contains "technical_reference" "${docLibs[@]}" || contains "all" "${docLibs[@]}"; then
  echo "Building Technical Reference..."
  rm -rf build/technical_reference || true
  sphinx-build -b html docs/technical_reference build/technical_reference
fi

if contains "user_guide" "${docLibs[@]}" || contains "all" "${docLibs[@]}"; then
  echo "Building User Guide..."
  rm -rf build/user_guide || true
  sphinx-build -b html docs/user_guide build/user_guide
fi

if contains "library" "${docLibs[@]}" || contains "all" "${docLibs[@]}"; then
  echo "Building Library Documentation..."
  rm -rf build/library || true
  # Note: PowerShell version outputs Library docs into 'build' (root), not 'build/library'
  sphinx-build -b html docs/library build
fi