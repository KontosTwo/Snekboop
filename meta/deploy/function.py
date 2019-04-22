import os
import redis
import json

def handler(event, context):
    redis_host = os.environ["REDIS_HOST"]
    redis_port = os.environ["REDIS_PORT"]

    sockets = event["sockets"]
    shard_level = int(event["shard_level"])

    pool = redis.ConnectionPool(host=redis_host, port=redis_port)
    r = redis.Redis(connection_pool=pool)

    pipe = r.pipeline()
    pipe.set("shard_level",shard_level)
    pipe.set("num_shards", len(sockets))
    pipe.set("global_shard_counter", 0)
    for i in range(len(sockets)):
        pipe.hset("shard", i, json.dumps(sockets[i]))
    if(shard_level > len(sockets)):
        message = {
            "statusCode": 400,
            "headers": {"Content-Type": "application/json"},
            "body": "The shard_level cannot be more than the number of sockets"
        }
        return message

    pipe.execute()

    message = {
        "statusCode": 201,
        "headers": {"Content-Type": "application/json"},
        "body": "Successfully deployed snekboop"
    }
    return message
