# pptoml

[![PyPI - Version](https://img.shields.io/pypi/v/pptoml.svg)](https://pypi.org/project/pptoml)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pptoml.svg)](https://pypi.org/project/pptoml)

Library and CLI tool for parsing, validating, modifying, and updating `pyproject.toml` files. 

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install pptoml
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
