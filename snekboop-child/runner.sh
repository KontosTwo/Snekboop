#!/usr/bin/env bash

export SNEKBOOP_CHILD_PORT=10001

source ./venv/bin/activate
python ./src/child.py