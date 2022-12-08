import json
from pathlib import Path

import rich
import rich.markup
import rich.pretty
import typer

import pptoml
from pptoml import MetaFormat

app = typer.Typer()


@app.callback()
def main_callback():
    """
    cli for pptoml
    """


@app.command()
def show(
    filepath: Path = typer.Argument(..., help='path to pyproject.toml file'),
    format: MetaFormat = typer.Option(MetaFormat.dict, help='format to print'),
    pretty: bool = typer.Option(True, help='prettify output')
) -> None:
    if format == MetaFormat.toml:
        with open(filepath) as f:
            for line in f:
                print(line, end='') if not pretty else rich.print(rich.markup.escape(line), end='')
    elif format == MetaFormat.dict:
        toml_dict = pptoml.load(filepath)
        print(toml_dict) if not pretty else rich.pretty.pprint(toml_dict)
    elif format == MetaFormat.json:
        toml_dict = pptoml.load(filepath)
        s = json.dumps(toml_dict)
        print(s) if not pretty else rich.print_json(s)


@app.command()
def get(
    filepath: Path = typer.Argument(..., help='path to pyproject.toml file'),
    field: str = typer.Argument(..., help='field to get')
) -> None:
    pass


@app.command()
def set(
    filepath: Path = typer.Argument(..., help='path to pyproject.toml file'),
    field: str = typer.Argument(..., help='field to set'),
    value: str = typer.Argument(..., help='value to set')
) -> None:
    """
    add new field or modify existing
    """
    pass


# validate with schema
# print general info
# generate new pyproject.toml with prompts
# add, remove dependencies
# check for dep updates
# update version
