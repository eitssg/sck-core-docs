# Copilot Instructions (Submodule: sck-core-docs)

- Tech: Sphinx documentation (Python-driven).
- Precedence: Local first; then root `../../.github/...`.
- Conventions: Keep docs consistent with UI/Backend contracts where referenced. Prefer reStructuredText for technical references, link to UI docs when UI behavior is discussed.

## Contradiction Detection
- Ensure content aligns with UI/Backend contracts and root precedence.
- If conflict, warn + options + example.
- Example: "Doc suggests storing tokens in localStorage, which conflicts with UI auth docs; correct to session cookie/access token in memory."

## Standalone clone note
If cloned standalone, see:
- UI/backend conventions: https://github.com/eitssg/simple-cloud-kit/tree/develop/sck-core-ui/docs
- Root Copilot guidance: https://github.com/eitssg/simple-cloud-kit/blob/develop/.github/copilot-instructions.md
 
# WARNING

## IMPORTANT

[REQUIRED] The sphinx documentation in this repo is NOT maintained.  This documenation should be generated from docstrings in the code and from the UI documentation in sck-core-ui.  Also, the users guide is from an old alpha version and is not up to date with the current codebase.  Please DO NOT UNDER ANY CIRCUMSTANCES REFERENCE documentation in this repo for style, formatting, or code development.  YOU MAY UPDATE THIS DOCUMEATION AT WILL and fix it.  

ALWAYS use the current code base as the source of truth and for any contradiction, use CODE as the source of truth FIRST, then docstrings SECOND, then for clarification, ALWAYS CONFIRM with the developer regarding dicisions from this documentation.