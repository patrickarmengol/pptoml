from enum import Enum
from pathlib import Path
from typing import Any

import tomli


class MetaFormat(str, Enum):
    toml = 'toml'
    json = 'json'
    dict = 'dict'


def load(filepath: Path) -> dict[str, Any]:
    with open(filepath, mode='rb') as f:
        return tomli.load(f)


# def dumps_json(toml_dict: dict[str, Any], pretty: bool = False) -> str:
#     return json.dumps(toml_dict) if not pretty else json.dumps(toml_dict, indent=4)


# def dumps_dict(toml_dict: dict[str, Any], pretty: bool = False) -> str:
#     return str(toml_dict) if not pretty else pprint.pformat(toml_dict)


def get(toml_dict: dict[str, Any], field: 'str') -> Any:
    pass


def set(toml_dict: dict[str, Any], field: 'str', value: Any) -> None:
    pass
