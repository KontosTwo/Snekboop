#!/usr/bin/env bash

export SNEKBOOP_API_PORT=10002
export SNEKBOOP_HUB_IP=127.0.0.1
export SNEKBOOP_HUB_PORT=10000

source ../venv/bin/activate
python ./src/api.py