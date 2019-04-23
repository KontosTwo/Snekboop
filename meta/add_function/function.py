import os
import redis
import json

def handler(event, context):
    redis_host = os.environ["REDIS_HOST"]
    redis_port = os.environ["REDIS_PORT"]

    pool = redis.ConnectionPool(host=redis_host, port=redis_port)
    r = redis.Redis(connection_pool=pool)

    name = event["func_name"]
    url = event["func_url"]

    func_exists = r.hexists("functions",name)
    if func_exists:
        message = {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": "Function name already exists"
        }
        return message

    r.hset("functions",name,url)

    message = {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": "Function added to snekboop"
    }
    return message
