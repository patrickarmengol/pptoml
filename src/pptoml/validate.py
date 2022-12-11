# validate pyproject.toml against a json schema or maybe taplo
from typing import Any

import validate_pyproject.api
import validate_pyproject.errors


def validate_config(config: dict[str, Any]) -> bool:
    validator = validate_pyproject.api.Validator()
    try:
        validator(config)
    except validate_pyproject.errors.ValidationError as ex:
        print(f'{ex}')
        return False
    return True
