#!/usr/bin/env python3
"""
Script to fix AI-generated docstrings with >>> syntax that cause Sphinx RST warnings.

This script converts interactive Python docstrings (with >>>) to proper RST format
that works with Sphinx documentation generation.
"""

import os
import re
import argparse
from pathlib import Path
from typing import List, Tuple


def fix_docstring_examples(content: str) -> Tuple[str, int]:
    """
    Fix docstring examples that use >>> syntax.

    More conservative approach that only touches examples sections within docstrings.

    Returns:
        Tuple of (fixed_content, number_of_fixes)
    """
    fixes_made = 0

    # Look for docstring blocks (triple quoted strings)
    in_docstring = False
    lines = content.split("\n")
    result_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check for start of docstring
        if '"""' in line and not in_docstring:
            in_docstring = True
            result_lines.append(line)
            i += 1
            continue

        # Check for end of docstring
        if '"""' in line and in_docstring:
            in_docstring = False
            result_lines.append(line)
            i += 1
            continue

        # If we're in a docstring and find an Examples section with >>>
        if (
            in_docstring
            and ("Examples" in line or "Example" in line)
            and ("---" in line or ":" in line)
        ):
            # Check if the next few lines contain >>> syntax
            has_interactive_examples = False
            j = i + 1
            while j < len(lines) and j < i + 10:  # Look ahead up to 10 lines
                if ">>>" in lines[j]:
                    has_interactive_examples = True
                    break
                if (
                    lines[j].strip()
                    and not lines[j].startswith("    ")
                    and not lines[j].startswith("\t")
                ):
                    break  # Hit next section
                j += 1

            if has_interactive_examples:
                # Fix this Examples section
                indent = len(line) - len(line.lstrip())
                if "---" in line:
                    # NumPy-style docstring - replace "Examples\n----" with "Examples::"
                    result_lines.append(" " * indent + "Examples::")
                    result_lines.append("")  # Add blank line after ::
                    # Skip the dashes line
                    if i + 1 < len(lines) and "---" in lines[i + 1]:
                        i += 1
                else:
                    # Standard docstring with colon
                    result_lines.append(" " * indent + line.strip().replace(":", "::"))
                    result_lines.append("")  # Add blank line after ::

                i += 1
                # Process the example lines
                while i < len(lines):
                    curr_line = lines[i]

                    # If we hit the end of examples (dedented line or empty line followed by dedented)
                    if curr_line.strip() == "":
                        result_lines.append(curr_line)
                        i += 1
                        continue

                    curr_indent = len(curr_line) - len(curr_line.lstrip())
                    if curr_indent <= indent and curr_line.strip():
                        break  # Next section started

                    stripped = curr_line.strip()
                    if stripped.startswith(">>> "):
                        # Code line - remove >>> and keep indentation
                        code = stripped[4:]
                        result_lines.append(" " * (indent + 4) + code)
                    elif stripped.startswith("..."):
                        # Continuation line
                        continuation = stripped[3:].lstrip()
                        if continuation:
                            result_lines.append(" " * (indent + 4) + continuation)
                    elif stripped and not stripped.startswith("#"):
                        # Output line - convert to comment
                        result_lines.append(
                            " " * (indent + 4) + f"# Returns: {stripped}"
                        )
                    else:
                        result_lines.append(curr_line)

                    i += 1

                fixes_made += 1
                continue

        result_lines.append(line)
        i += 1

    return "\n".join(result_lines), fixes_made


def process_file(file_path: Path) -> Tuple[int, bool]:
    """
    Process a single Python file to fix docstring issues.

    Returns:
        Tuple of (number_of_fixes, file_was_modified)
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            original_content = f.read()

        fixed_content, fixes_made = fix_docstring_examples(original_content)

        if fixes_made > 0:
            # Write back the fixed content
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(fixed_content)
            print(f"Fixed {fixes_made} docstring examples in {file_path}")
            return fixes_made, True

        return 0, False

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return 0, False


def process_single_file(file_path: str, dry_run: bool = False) -> Tuple[int, bool]:
    """Process a single file by path."""
    file_obj = Path(file_path)
    if not file_obj.exists() or not file_obj.suffix == ".py":
        print(f"File {file_path} does not exist or is not a Python file")
        return 0, False

    if dry_run:
        try:
            with open(file_obj, "r", encoding="utf-8") as f:
                content = f.read()
            _, fixes = fix_docstring_examples(content)
            if fixes > 0:
                print(f"Would fix {fixes} docstring examples in {file_path}")
                return fixes, True
            return 0, False
        except Exception as e:
            print(f"Error checking {file_path}: {e}")
            return 0, False
    else:
        return process_file(file_obj)


def find_python_files(directory: Path) -> List[Path]:
    """Find all Python files in directory recursively."""
    python_files = []
    for root, dirs, files in os.walk(directory):
        # Skip certain directories
        dirs[:] = [
            d
            for d in dirs
            if not d.startswith(".") and d not in ["__pycache__", "node_modules"]
        ]

        for file in files:
            if file.endswith(".py"):
                python_files.append(Path(root) / file)

    return python_files


def main():
    parser = argparse.ArgumentParser(
        description="Fix AI-generated docstrings with >>> syntax"
    )
    parser.add_argument(
        "path", help="Directory to process (recursively) or single Python file"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be fixed without making changes",
    )

    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        print(f"Path {path} does not exist")
        return 1

    total_fixes = 0
    files_modified = 0

    if path.is_file():
        fixes, modified = process_single_file(str(path), args.dry_run)
        total_fixes += fixes
        if modified:
            files_modified += 1
    else:
        python_files = find_python_files(path)
        print(f"Found {len(python_files)} Python files to process")

        for file_path in python_files:
            if args.dry_run:
                # For dry run, just check what would be fixed
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    _, fixes = fix_docstring_examples(content)
                    if fixes > 0:
                        print(f"Would fix {fixes} docstring examples in {file_path}")
                        total_fixes += fixes
                        files_modified += 1
                except Exception as e:
                    print(f"Error checking {file_path}: {e}")
            else:
                fixes, modified = process_file(file_path)
                total_fixes += fixes
                if modified:
                    files_modified += 1

    action = "Would fix" if args.dry_run else "Fixed"
    print(f"\n{action} {total_fixes} docstring examples in {files_modified} files")

    return 0


if __name__ == "__main__":
    exit(main())
