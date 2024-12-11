<!--
  ~ Copyright (c) 2023-2024 Datalayer, Inc.
  ~
  ~ BSD 3-Clause License
-->

[![Datalayer](https://assets.datalayer.tech/datalayer-25.svg)](https://datalayer.io)

[![Become a Sponsor](https://img.shields.io/static/v1?label=Become%20a%20Sponsor&message=%E2%9D%A4&logo=GitHub&style=flat&color=1ABC9C)](https://github.com/sponsors/datalayer)

[![Github Actions Status](https://github.com/datalayer/jupyter-ai-agent/workflows/Build/badge.svg)](https://github.com/datalayer/jupyter-ai-agent/actions/workflows/build.yml)

# 🪐 🤖 Jupyter AI Agent

*Use Jupyter AI Agent, an AI Agent equipped with tools like 'execute', 'insert_cell', and more, to transform your notebooks into an intelligent, interactive workspace!*

![Jupyter AI Agent](https://assets.datalayer.tech/jupyter-ai-agent/ai-agent-jupyterlab.gif)

Jupyter AI Agent empowers **AI** models to **interact** with and **modify Jupyter notebooks**. The model is equipped with tools such as adding code cells, inserting markdown cells, executing code, enabling it to modify the notebook comprehensively based on user instructions. This agent is **innovative** as it is designed to **operate on the entire notebook**, not just at the cell level, enabling more comprehensive and seamless modifications.

This powerful functionality is made possible through [jupyter-nbmodel-client](https://github.com/datalayer/jupyter-nbmodel-client) and [jupyter-kernel-client](https://github.com/datalayer/jupyter-kernel-client), enabling interaction with Jupyter notebooks and kernels.

> [!WARNING] 
> jupyter-nbmodel-client and jupyter-kernel-client are experimental and under active development. 
> Unexepected behavior such as ["Panic Exception"](https://github.com/datalayer/jupyter-nbmodel-client/issues/12) may occur.

[LangChain agent framework](https://python.langchain.com/v0.1/docs/modules/agents/how_to/custom_agent/) is used to manage the interactions between the AI model and the tools.

> [!IMPORTANT] 
> Jupyter AI Agent currently only supports models from Azure OpenAI.

## Install

To install Jupyter AI Agent, execute:

```bash
pip install jupyter_ai_agent
```

## Usage

### Example 1: JupyterLab

![Jupyter AI Agent](https://assets.datalayer.tech/jupyter-ai-agent/ai-agent-jupyterlab.gif)

The Jupyter AI Agent can directly interact with JupyterLab and the modifications made by the Jupyter AI Agent can be seen in real-time thanks to [Jupyter real time collaboration](https://jupyterlab.readthedocs.io/en/stable/user/rtc.html).

```
Jupyter AI Agent <---> JupyterLab
    |            (rtc)
JNC   JKC
```

First, make sure you have JupyterLab installed:

```bash
pip install jupyterlab
```

Then, start JupyterLab:

```bash
jupyter lab
```
Then, make sure you have a `.env` file with the following content:

```bash
OPENAI_API_VERSION = ...
AZURE_OPENAI_ENDPOINT = ...
AZURE_OPENAI_API_KEY = ...
```

To use the Jupyter AI Agent, execute the following:

```python
azure_deployment_name = "gpt-4o-mini" # for example
server_url = "http://localhost:8888" # for example, typical when using JupyterLab
token = "..." # your JupyterLab token
notebook_path = "..." # the path to the notebook you want the Jupyter AI Agent to modify

input = '''
Scrape historical stock price data for Apple from Yahoo Finance. 
The data should include columns like Date, Open, High, Low, Close, and Volume. 
After scraping, visualize the data with a line chart showing the closing prices over time.
''' # the input to the Jupyter AI Agent

ask_agent(server_url, token, azure_deployment_name, notebook_path, input)
````

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
