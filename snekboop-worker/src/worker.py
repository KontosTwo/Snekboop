import redis
import json
import rpyc
import os

worker_port = None

try:
    worker_port = os.environ["SNEKBOOP_WORKER_PORT"]
except:
    print("Failed initialization. The environment variable SNEKBOOP_WORKER_PORT must be defined")
    exit(1)

access_key = None

try:
    access_key = os.environ["AWS_ACCESS_KEY_ID"]
except:
    print("Failed initialization. The environment variable AWS_ACCESS_KEY_ID must be defined")
    exit(1)

secret_key = None

try:
    secret_key = os.environ["AWS_SECRET_ACCESS_KEY"]
except:
    print("Failed initialization. The environment variable AWS_SECRET_ACCESS_KEY must be defined")
    exit(1)


