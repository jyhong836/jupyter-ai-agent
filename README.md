<!--
  ~ Copyright (c) 2023-2024 Datalayer, Inc.
  ~
  ~ BSD 3-Clause License
-->

[![Datalayer](https://assets.datalayer.tech/datalayer-25.svg)](https://datalayer.io)

[![Become a Sponsor](https://img.shields.io/static/v1?label=Become%20a%20Sponsor&message=%E2%9D%A4&logo=GitHub&style=flat&color=1ABC9C)](https://github.com/sponsors/datalayer)

[![Github Actions Status](https://github.com/datalayer/jupyter-ai-agent/workflows/Build/badge.svg)](https://github.com/datalayer/jupyter-ai-agent/actions/workflows/build.yml)

# 🪐 🤖 Jupyter AI Agent

Jupyter AI Agent.

## Requirements

- Jupyter Server with ipykernel running somewhere.
  You can install those packages using:

```sh
pip install jupyter-server ipykernel
```

## Install

To install the extension, execute:

```bash
pip install jupyter_ai_agent
```

## Usage

..

## Uninstall

To remove the extension, execute:

```bash
pip uninstall jupyter_ai_agent
```

## Troubleshoot

If you are seeing the frontend extension, but it is not working, check
that the server extension is enabled:

```bash
jupyter server extension list
```

## Contributing

### Development install

```bash
# Clone the repo to your local environment
# Change directory to the jupyter_ai_agent directory
# Install package in development mode - will automatically enable
# The server extension.
pip install -e ".[test,lint,typing]"
```

### Running Tests

Install dependencies:

```bash
pip install -e ".[test]"
```

To run the python tests, use:

```bash
pytest
```

### Development uninstall

```bash
pip uninstall jupyter_ai_agent
```

### Packaging the extension

See [RELEASE](RELEASE.md)
