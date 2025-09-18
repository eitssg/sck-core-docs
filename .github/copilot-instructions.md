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
 
