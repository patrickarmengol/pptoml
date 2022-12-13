import json
from pathlib import Path
from typing import Callable, Union

import questionary
import rich
import rich.markup
import rich.pretty
import typer

from pptoml.enums import (Backend, Formatter, License, Linter, MetaFormat,
                          TypeChecker)
from pptoml.fetch import fetch_info
from pptoml.generate import GenSettings, generate_config
from pptoml.inout import load_config
from pptoml.validate import validate_config

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


@app.command()
def new(
    output_path: Path = typer.Option(None, help='desired path for output file'),  # TODO: path checks
) -> None:
    """
    generate a pyproject.toml file
    """

    val_not_empty_str: Callable[[str], Union[bool, str]] = lambda x: True if len(x) > 0 else 'must not be empty'
    val_numeric_str: Callable[[str], Union[bool, str]] = lambda x: True if x.isnumeric() else 'must be an integer'

    answers = questionary.form(
        backend=questionary.select(message='backend: ', choices=[m.value for m in Backend]),
        project_name=questionary.text(message='project name: ', validate=val_not_empty_str),
        project_description=questionary.text(message='project description: ', validate=val_not_empty_str),
        licenses=questionary.checkbox(message='licenses: ', choices=[m.value for m in License]),
        author_name=questionary.text(message='author name: ', validate=val_not_empty_str),
        author_email=questionary.text(message='author email: ', validate=val_not_empty_str),
        github_username=questionary.text(message='github username (for urls): '),
        tools=questionary.checkbox(message='tools: ', choices=[questionary.Choice(
            title=f'{m.value} ({type(m).__name__})', value=m.value) for e in [TypeChecker, Linter, Formatter] for m in e]),
        max_line_length=questionary.text(message='max line length (for tools): ',
                                         validate=val_numeric_str,),  # how do i convert this here?
    ).ask()

    # print(answers)

    # TODO: accept kwargs from commandline
    settings = GenSettings(**answers)

    config_str = generate_config(settings)

    if output_path:
        output_path.write_text(config_str)
        print(f'config written to {output_path}')
    else:
        print(config_str)  # enables piping to file in commandline
