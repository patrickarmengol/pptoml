import json
from enum import Enum
from pathlib import Path

import rich
import rich.markup
import rich.pretty
import typer

from pptoml.fetch import fetch_info
from pptoml.inout import load_config
from pptoml.validate import validate_config


class MetaFormat(str, Enum):
    toml = 'toml'
    json = 'json'
    dict = 'dict'


app = typer.Typer()


@app.callback()
def main_callback():
    """
    cli for pptoml
    """


@app.command()
def info(
    filepath: Path = typer.Option(Path('./pyproject.toml'), help='path to pyproject.toml file'),
) -> None:
    """
    fetch generally useful info about the project from the pyproject config
    """
    config = load_config(filepath)
    info = fetch_info(config)
    for k, v in info.items():
        if type(v) == list:  # how do i make sure the elements are strings?
            v = ', '.join(v)
        rich.print(f'{k:30}{v}')  # should i stringify v?


@app.command()
def dump(
    format: MetaFormat = typer.Option(MetaFormat.dict, help='format to print'),
    pretty: bool = typer.Option(True, help='prettify output'),
    filepath: Path = typer.Option(Path('./pyproject.toml'), help='path to pyproject.toml file',
                                  exists=True, file_okay=True, dir_okay=False)
) -> None:
    """
    print pyproject config in specified format
    """
    if format == MetaFormat.toml:
        s = filepath.read_text(encoding='utf-8')
        print(s) if not pretty else rich.print(rich.markup.escape(s))
    elif format == MetaFormat.dict:
        config = load_config(filepath)
        print(config) if not pretty else rich.print(config)
    elif format == MetaFormat.json:
        config = load_config(filepath)
        s = json.dumps(config)
        print(s) if not pretty else rich.print_json(s)


@app.command()
def get(
    field: str = typer.Argument(..., help='field to get'),
    filepath: Path = typer.Option(Path('./pyproject.toml'), help='path to pyproject.toml file'),
) -> None:
    """
    print the value of the specified field
    """
    pass


@app.command()
def validate(
    filepath: Path = typer.Option(Path('./pyproject.toml'), help='path to pyproject.toml file'),
) -> None:
    """
    validate pyproject against PEP specifications
    """
    config = load_config(filepath)
    print('config is', 'valid' if validate_config(config) else 'invalid')
