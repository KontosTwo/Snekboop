import os
import redis
import json

def handler(event, context):
    redis_host = os.environ["REDIS_HOST"]
    redis_port = os.environ["REDIS_PORT"]

    pool = redis.ConnectionPool(host=redis_host, port=redis_port)
    r = redis.Redis(connection_pool=pool)

    name = event["func_name"]

    func_exists = r.hexists("functions",name)
    if not func_exists:
        message = {
            "statusCode": 404,
            "headers": {"Content-Type": "application/json"},
            "body": "Function name does not exist"
        }
        return message

    url = r.hget("functions",name).decode("utf-8")

    message = {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": url
    }
    return message
