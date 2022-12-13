from typing import TypedDict

from pptoml.enums import Backend, Formatter, License, Linter, TypeChecker

TEMPLATE = """
[build-system]
requires = ["{build_req}"]
build-backend = "{build_backend}"

[project]
name = "{project_name}"
version = "0.0.1"
description = '{project_description}'
readme = "README.md"
requires-python = ">=3.7"
license = "{licenses}"
license-files = {{ globs = ["LICENSE*"] }}
keywords = []
authors = [
  {{ name = "{author_name}", email = "{author_email}" }},
]
classifiers = [
  "Development Status :: 4 - Beta",
  "Programming Language :: Python",
  "Programming Language :: Python :: 3.7",
  "Programming Language :: Python :: 3.8",
  "Programming Language :: Python :: 3.9",
  "Programming Language :: Python :: 3.10",
  "Programming Language :: Python :: 3.11",
  "Programming Language :: Python :: Implementation :: CPython",
  "Programming Language :: Python :: Implementation :: PyPy",
]
dependencies = []

[project.scripts]

[project.urls]
Documentation = "https://github.com/{github_username}/{project_name}#readme"
Issues = "https://github.com/{github_username}/{project_name}/issues"
Source = "https://github.com/{github_username}/{project_name}"
"""

PYRIGHT_TEMPLATE = """
[tool.pyright]
include = ["src/pptoml", "tests"]
exclude = [
    "**/__pycache__",
]
typeCheckingMode = "strict"
"""

MYPY_TEMPLATE = """
[tool.mypy]
include = ["src/pptoml", "tests"]
exclude = [
    "**/__pycache__",
]
strict = true
"""

RUFF_TEMPLATE = """
[tool.ruff]
target-version = "py37"
line-length = {max_line_length}
select = ["A", "B", "C", "E", "F", "FBT", "I", "N", "Q", "RUF", "S", "T", "UP", "W", "YTT"]
ignore = [
  # Allow non-abstract empty methods in abstract base classes
  "B027",
  # Ignore McCabe complexity
  "C901",
  # Allow boolean positional values in function calls, like `dict.get(... True)`
  "FBT003",
  # Ignore checks for possible passwords
  "S105", "S106", "S107",
]
unfixable = [
  # Don't touch unused imports
  "F401",
]

[tool.ruff.isort]
known-first-party = ["pptoml"]

[tool.ruff.flake8-tidy-imports]
ban-relative-imports = "all"

[tool.ruff.per-file-ignores]
# Tests can use relative imports and assertions
"tests/**/*" = ["I252", "S101"]
"""

AUTOPEP8_TEMPLATE = """
[tool.autopep8]
max_line_length = {max_line_length}
"""

BLACK_TEMPLATE = """
[tool.black]
target-version = ["py37"]
line-length = {max_line_length}
skip-string-normalization = true
"""

BLUE_TEMPLATE = """
[tool.blue]
target-version = ["py37"]
line-length = {max_line_length}
"""


class GenSettings(TypedDict):
    backend: Backend
    project_name: str
    project_description: str
    licenses: list[License]
    author_name: str
    author_email: str
    github_username: str
    tools: list[TypeChecker | Linter | Formatter]
    max_line_length: int | str
    # TODO: add python version setting


def generate_config(settings: GenSettings, custom_template: str | None = None) -> str:
    base_template = custom_template if custom_template else TEMPLATE

    match settings['backend']:
        case Backend.hatchling:
            build_req = 'hatchling'
            build_backend = 'hatchling.build'
        case Backend.setuptools:
            build_req = 'setuptools'
            build_backend = 'setuptools.build_meta'

    filled = base_template.format(
        build_req=build_req,
        build_backend=build_backend,
        project_name=settings['project_name'],
        project_description=settings['project_description'],
        licenses=' OR '.join(settings['licenses']),
        author_name=settings['author_name'],
        author_email=settings['author_email'],
        github_username=settings['github_username'] if settings['github_username'] != '' else 'unknown'
    )

    for tool in settings['tools']:
        match tool:
            case TypeChecker.pyright:
                filled += PYRIGHT_TEMPLATE
            case TypeChecker.mypy:
                filled += MYPY_TEMPLATE
            case Linter.ruff:
                filled += RUFF_TEMPLATE.format(max_line_length=settings['max_line_length'])
            case Formatter.autopep8:
                filled += AUTOPEP8_TEMPLATE.format(max_line_length=settings['max_line_length'])
            case Formatter.black:
                filled += BLACK_TEMPLATE.format(max_line_length=settings['max_line_length'])
            case Formatter.blue:
                filled += BLUE_TEMPLATE.format(max_line_length=settings['max_line_length'])

    return filled
