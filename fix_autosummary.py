#!/usr/bin/env python3
"""
Script to replace autosummary directives with automodule directives
to eliminate duplicate documentation warnings.
"""
import os
import re
import glob


def replace_autosummary_in_file(filepath):
    """Replace autosummary directives with automodule directives in a single file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Find the module name from the autosummary directive
    autosummary_pattern = r"\.\.[ ]+autosummary::\s*\n(?:\s+:[^:]+:[^\n]*\n)*\s+([a-zA-Z_][a-zA-Z0-9_]*(?:\.[a-zA-Z_][a-zA-Z0-9_]*)*)"

    def replace_func(match):
        module_name = match.group(1)
        return f""".. automodule:: {module_name}
   :members:
   :undoc-members:
   :show-inheritance:"""

    # Replace autosummary blocks
    new_content = re.sub(autosummary_pattern, replace_func, content, flags=re.MULTILINE)

    if new_content != content:
        print(f"Updated: {filepath}")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    return False


def main():
    """Process all RST files in technical_reference."""
    rst_files = glob.glob("docs/technical_reference/**/*.rst", recursive=True)

    updated_files = 0
    for filepath in rst_files:
        if replace_autosummary_in_file(filepath):
            updated_files += 1

    print(f"Updated {updated_files} files")


if __name__ == "__main__":
    main()
