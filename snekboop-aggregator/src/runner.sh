#!/usr/bin/env bash

docker build -t snekboop-aggregator .
docker run snekboop-aggregator -e AWS_ACCESS_KEY_ID=1e2esg24g AWS_SECRET_ACCESS_KEY=asdf786asg876 SNEKBOOP_AGGREGATOR_PORT=10001
