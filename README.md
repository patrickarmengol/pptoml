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
from pptoml.inout import load
from pptoml.fetch import fetch_info

config = load(Path('path/to/pyproject.toml'))
info = fetch_info(config)
```

### as a cli app
```console                                        
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
╰─────────────────────────────────────────────────────╯
```

## Roadmap

### 0.1.0

- [x] fetch general info for the project
- [x] dump config in various formats

### 0.2.0

- [ ] validate with schema

### 0.3.0

- [ ] generate new pyproject.toml with prompts

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
