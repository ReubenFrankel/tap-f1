# tap-f1

`tap-f1` is a Singer tap for F1.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

[![Python version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FReubenFrankel%2Ftap-f1%2Fmain%2Fpyproject.toml&query=tool.poetry.dependencies.python&label=python)](https://docs.python.org/3/)
[![Singer SDK version](https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FReubenFrankel%2Ftap-f1%2Fmain%2Fpyproject.toml&query=tool.poetry.dependencies%5B%22singer-sdk%22%5D.version&label=singer-sdk)](https://sdk.meltano.com/en/latest/)
[![License](https://img.shields.io/github/license/ReubenFrankel/tap-f1)](https://github.com/ReubenFrankel/tap-f1/blob/main/LICENSE)
[![Code style](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2Fastral-sh%2Fruff%2Fmain%2Fassets%2Fbadge%2Fformat.json)](https://docs.astral.sh/ruff/)
[![Test tap-f1](https://github.com/ReubenFrankel/tap-f1/actions/workflows/test.yml/badge.svg)](https://github.com/ReubenFrankel/tap-f1/actions/workflows/test.yml)

<!--

Developer TODO: Update the below as needed to correctly describe the install procedure. For instance, if you do not have a PyPi repo, or if you want users to directly install from your git repo, you can modify this step as appropriate.

## Installation

Install from PyPi:

```bash
pipx install tap-f1
```

Install from GitHub:

```bash
pipx install git+https://github.com/ORG_NAME/tap-f1.git@main
```

-->

## Configuration

### Accepted Config Options

<!--
Developer TODO: Provide a list of config options accepted by the tap.

This section can be created by copy-pasting the CLI output from:

```
tap-f1 --about --format=markdown
```
-->

A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-f1 --about
```

### Configure using environment variables

This Singer tap will automatically import any environment variables within the working directory's
`.env` if the `--config=ENV` is provided, such that config values will be considered if a matching
environment variable is set either in the terminal context or in the `.env` file.

### Source Authentication and Authorization

<!--
Developer TODO: If your tap requires special access on the source system, or any special authentication requirements, provide those here.
-->

## Usage

You can easily run `tap-f1` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-f1 --version
tap-f1 --help
tap-f1 --config CONFIG --discover > ./catalog.json
```

## Developer Resources

Follow these instructions to contribute to this project.

### Initialize your Development Environment

Prerequisites:

- Python 3.9+
- [uv](https://docs.astral.sh/uv/)

```bash
uv sync
```

### Create and Run Tests

Create tests within the `tests` subfolder and
  then run:

```bash
uv run pytest
```

You can also test the `tap-f1` CLI interface directly using `uv run`:

```bash
uv run tap-f1 --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

<!--
Developer TODO:
Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any "TODO" items listed in
the file.
-->

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-f1
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-f1 --version
# OR run a test `elt` pipeline:
meltano elt tap-f1 target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to
develop your own taps and targets.
