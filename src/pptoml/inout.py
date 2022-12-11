# parsing and dumping pyproject.toml

import json
from pathlib import Path
from pprint import pformat
from typing import Any

import tomli


def load(filepath: Path) -> dict[str, Any]:
    with filepath.open(mode='rb') as f:
        return tomli.load(f)


def dumps_json(toml_dict: dict[str, Any], pretty: bool = False) -> str:
    return json.dumps(toml_dict) if not pretty else json.dumps(toml_dict, indent=4)


def dumps_dict(toml_dict: dict[str, Any], pretty: bool = False) -> str:
    return str(toml_dict) if not pretty else pformat(toml_dict)
