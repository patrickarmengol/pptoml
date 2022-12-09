import json
from pathlib import Path

import rich
import rich.markup
import rich.pretty
import typer

from pptoml.inout import MetaFormat, load

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
    pass


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
        toml_dict = load(filepath)
        print(toml_dict) if not pretty else rich.pretty.pprint(toml_dict)
    elif format == MetaFormat.json:
        toml_dict = load(filepath)
        s = json.dumps(toml_dict)
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
def set(
    field: str = typer.Argument(..., help='field to set'),
    value: str = typer.Argument(..., help='value to set'),
    filepath: Path = typer.Option(Path('./pyproject.toml'), help='path to pyproject.toml file'),
) -> None:
    """
    add new field or modify existing
    """
    pass


@app.command()
def validate(
    filepath: Path = typer.Argument(..., help='path to pyproject.toml file'),
) -> None:
    """
    validate pyproject against PEP specifications
    """
    pass
