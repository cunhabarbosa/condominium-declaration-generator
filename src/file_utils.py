"""Utilities for validating file existence and handling overwrite confirmations."""

from pathlib import Path
import sys


def validate_file_exists(file_path: str | Path, description: str) -> Path:
    """
    Validate that a required file exists.

    Args:
        file_path: Path to the file
        description: Human-readable description of the file

    Returns:
        Path object if the file exists

    Raises:
        SystemExit if the file does not exist
    """

    path = Path(file_path)

    if not path.exists():
        print(f"ERROR: {description} not found: {path}")
        sys.exit(1)

    if not path.is_file():
        print(f"ERROR: {description} is not a file: {path}")
        sys.exit(1)

    return path

def confirm_overwrite(path: Path) -> bool:
    """Ask user confirmation before overwriting an existing file."""
    if not path.exists():
        return True

    answer = input(f"File already exists: {path}\nOverwrite? (y/n): ").strip().lower()
    return answer in ("y", "yes")
