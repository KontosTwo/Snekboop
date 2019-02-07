#!/usr/bin/env bash

docker build -t snekboop-api .
docker run snekboop-api -e AWS_ACCESS_KEY_ID=1e2esg24g AWS_SECRET_ACCESS_KEY=asdf786asg876 SNEKBOOP_API_PORT=100001
