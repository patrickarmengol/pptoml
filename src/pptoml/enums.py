from enum import Enum


class MetaFormat(str, Enum):
    toml = 'toml'
    json = 'json'
    dict = 'dict'


class Backend(str, Enum):
    hatchling = 'hatchling'
    setuptools = 'setuptools'


class License(str, Enum):
    apache = 'Apache-2.0'
    mit = 'MIT'


class TypeChecker(str, Enum):
    pyright = 'pyright'
    mypy = 'mypy'
    # TODO: add more


class Linter(str, Enum):
    ruff = 'ruff'
    # TODO: add more


class Formatter(str, Enum):
    autopep8 = 'autopep8'
    black = 'black'
    blue = 'blue'
    # TODO: add more
