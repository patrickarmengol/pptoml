# modify fields by getting and setting

from typing import Any


def get_field(toml_dict: dict[str, Any], field: str) -> Any:
    pass


def set_field(toml_dict: dict[str, Any], field: str, value: Any) -> None:
    pass


# welp i think tomlkit typing is broken
# hmmm... i don't want my every line of my code to be underlined in red
# i also don't want to not use typing
# file modifications is on hiatus until https://github.com/sdispater/tomlkit/issues/254 is resolved
