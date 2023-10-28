#!/bin/bash
# Included as a barebones example. IRL you'll probably be doing this part in a CICD pipeline.
set -x  # So you can see the commands as they run.

python3 -m venv venv-install
source venv-install/bin/activate
python3 -m pip install -U pip   # pip _always_ seems to need updating.
python -m pip install .