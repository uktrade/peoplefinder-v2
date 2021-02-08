#!/bin/bash

set -ex

# Local setup
virtualenv --python=python3 .venv

source .venv/bin/activate

pip install -r requirements.txt

deactivate

# Docker setup
make build
