#!/usr/bin/env bash
export $(cat .env | xargs)
docker-compose up --build --scale virtual_worker=${SNEKBOOP_LOCAL_PARTITIONS}