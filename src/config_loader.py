"""Configuration loading utilities."""

import json
from pathlib import Path
from typing import Any, Dict


def load_config(config_file: str | Path) -> Dict[str, Any]:
    """Load configuration from a JSON file."""
    with open(config_file, "r", encoding="utf-8") as file:
        return json.load(file)
