# pptoml

[![PyPI - Version](https://img.shields.io/pypi/v/pptoml.svg)](https://pypi.org/project/pptoml)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pptoml.svg)](https://pypi.org/project/pptoml)

Library and CLI tool for parsing, validating, modifying, and updating `pyproject.toml` files. 

-----

**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [License](#license)

## Installation

### as a module

```console
<virtual environment shenanigans>
pip install pptoml
```

### as a cli app

```console
pipx install pptoml
```

## Usage

### as a module
```python
from pathlib import Path
from pptoml.inout import load_config
from pptoml.fetch import fetch_info

config = load_config(Path('path/to/pyproject.toml'))
info = fetch_info(config)
```

### as a cli app

```console                                        
$ pptoml --help

 Usage: pptoml [OPTIONS] COMMAND [ARGS]...

 cli for pptoml

╭─ Options ───────────────────────────────────────────╮
│ --install-completion          Install completion    │
│                               for the current       │
│                               shell.                │
│ --show-completion             Show completion for   │
│                               the current shell, to │
│                               copy it or customize  │
│                               the installation.     │
│ --help                        Show this message and │
│                               exit.                 │
╰─────────────────────────────────────────────────────╯
╭─ Commands ──────────────────────────────────────────╮
│ dump      print pyproject config in specified       │
│           format                                    │
│ get       print the value of the specified field    │
│ info      fetch generally useful info about the     │
│           project from the pyproject config         │
│ new       generate a pyproject.toml file            │
│ validate  validate pyproject against PEP            │
│           specifications                            │
╰─────────────────────────────────────────────────────╯
```

#### example info fetch

```console
$ pptoml info
name                          pptoml
description                   Library and CLI tool for parsing, validating, modifying, and updating `pyproject.toml` files. 
authors                       Patrick Armengol
python_version                >=3.7
dependencies                  typer, tomli, validate-pyproject, questionary
license                       Apache-2.0 OR MIT
multi_licensed                True
scripts                       pptoml
docs_url                      https://github.com/patrickarmengol/pptoml#readme
issues_url                    https://github.com/patrickarmengol/pptoml/issues
source_url                    https://github.com/patrickarmengol/pptoml
build_backend                 hatchling
type_checking                 pyright
formatting                    autopep8
linting                       ruff
testing                       coverage
other_tools                   hatch
```



#### example new pyproject.toml generation

```console
$ pptoml new
? backend:  hatchling
? project name:  asdf
? project description:  does something i think
? licenses:  [MIT]
? author name:  Pat Cat
? author email:  pat@cat.cat
? github username (for urls):  patthecat
? tools:  done (3 selections)
? max line length (for tools):  120
```

```toml
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "asdf"
version = "0.0.1"
description = 'does something i think'
readme = "README.md"
requires-python = ">=3.7"
license = "MIT"
license-files = { globs = ["LICENSE*"] }
keywords = []
authors = [
  { name = "Pat Cat", email = "pat@cat.cat" },
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
Documentation = "https://github.com/patthecat/asdf#readme"
Issues = "https://github.com/patthecat/asdf/issues"
Source = "https://github.com/patthecat/asdf"

[tool.pyright]
include = ["src/pptoml", "tests"]
exclude = [
    "**/__pycache__",
]
typeCheckingMode = "strict"

[tool.ruff]
target-version = "py37"
line-length = 120
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

[tool.autopep8]
max_line_length = 120
```




## Roadmap

### 0.1.0

- [x] fetch general info for the project
- [x] dump config in various formats

### 0.2.0

> using existing validate-pyproject library to validate
>
> postponed support for PEP 639, tracked in https://github.com/abravalheri/validate-pyproject/issues/70

- [x] validate with schema

### 0.3.0

- [x] generate new pyproject.toml with prompts

### 0.4.0

> the following depend on tomlkit, which is a bit broken for type hinting atm

- [ ] update version
- [ ] add, remove dependencies

### 0.5.0

- [ ] check for dep updates


## License

`pptoml` is distributed under the terms of any of the following licenses:

- [Apache-2.0](https://spdx.org/licenses/Apache-2.0.html)
- [MIT](https://spdx.org/licenses/MIT.html)
