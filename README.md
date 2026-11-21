# tinyEmber

![CI](https://img.shields.io/github/actions/workflow/status/rkissgic/tinyEmber/ci.yml?branch=main&label=CI) ![Python](https://img.shields.io/badge/python-3.9+-blue) ![License](https://img.shields.io/github/license/rkissgic/tinyEmber?color=blue) ![Version](https://img.shields.io/badge/version-1.9.3-green)

A fast, type-annotated CLI utility built with Click and Rich. tinyEmber automates repetitive text-processing workflows -- read a file, apply transformations (trim, uppercase, enumerate lines), and write results. Configurable via YAML config files with a plugin-ready architecture.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [Changelog](#changelog)
- [License](#license)

## Features

- Click-based CLI with --input, --output, --config, and --verbose options
- Line-by-line text processing with configurable trim, uppercase, and line numbering
- Full type annotations with mypy/pyright compatibility
- Stdin support for piping: `cat data.txt | tinyEmber --output -`
- Cross-platform: tested on Linux, macOS, and Windows
- Pytest test suite with coverage for core processing logic

## Prerequisites

- Python 3.9 or higher
- pip or pipx for installation

## Installation

```bash
pip install tinyEmber
# or
pipx install tinyEmber
# or from source
git clone https://github.com/rkissgic/tinyEmber.git
cd tinyEmber && pip install -e .
```

## Usage

```bash
# Process a file with default settings
tinyEmber --input data.txt --output result.txt

# Use a YAML config file and verbose logging
tinyEmber --config config.yaml --verbose

# Pipe from stdin
cat data.txt | tinyEmber --output -

# Show help and version
tinyEmber --help
tinyEmber --version
```

The processing pipeline reads each line, trims whitespace, optionally uppercases, and adds line numbers:
```
0001 | Hello World
0002 | Foo Bar
```

## Project Structure

```
tinyEmber/
├── src/tinyEmber/
│   ├── __init__.py
│   └── cli.py
├── tests/
│   └── test_cli.py
├── pyproject.toml
├── README.md  LICENSE  CHANGELOG.md  CONTRIBUTING.md  CODE_OF_CONDUCT.md
├── .github/
│   ├── workflows/ci.yml
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   └── feature_request.md
│   └── PULL_REQUEST_TEMPLATE.md
└── .gitignore
```

## Running Tests

```bash
pytest
# with coverage report
pytest --cov=src --cov-report=term-missing
```

## Contributing

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

Quick start:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Make your changes and run tests (see [Running Tests](#running-tests) above)
4. Commit with a clear message: `git commit -am 'Add: my feature'`
5. Push to your fork: `git push origin feature/my-feature`
6. Open a Pull Request

Please ensure all tests pass before submitting a pull request.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes and version history.

## License

This project is licensed under the GPL-3.0 -- see the [LICENSE](LICENSE) file for details.

Copyright (c) 2026 chen kumar.

## Acknowledgements

- Built with Click, Rich, and PyYAML
- CI/CD powered by [GitHub Actions](https://github.com/features/actions)
- Badges by [shields.io](https://shields.io)
- Inspired by best practices from the open-source community
