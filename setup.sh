#!/bin/bash

set -ex

# Git config
git config core.hooksPath .githooks

# Local setup
virtualenv --python=python3 .venv

source .venv/bin/activate

pip install -r requirements.txt -r requirements-dev.txt

deactivate

# Docker setup
make build
