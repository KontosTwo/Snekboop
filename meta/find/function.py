import os
import redis
import json

def handler(event, context):
    redis_host = os.environ["REDIS_HOST"]
    redis_port = os.environ["REDIS_PORT"]

    pool = redis.ConnectionPool(host=redis_host, port=redis_port)
    r = redis.Redis(connection_pool=pool)

    name = event["name"]

    pipe = r.pipeline()
    pipe.get("shard_level")
    pipe.hexists("name", name)
    results = pipe.execute()
    shard_level = int(results[0])
    name_exists = results[1]
    if not name_exists:
        incr_shard = r.incr("global_shard_counter")
        if incr_shard >= shard_level:
            incr_shard = 0
            r.set("global_shard_counter", 0)
        pipe = r.pipeline()
        pipe.hset("name", name, 0)
        pipe.hset("shard_counter", name, incr_shard)
        pipe.execute()

    shard_counter = int(r.hget("shard_counter", name))
    num_shards = int(r.get("num_shards"))

    pipe = r.pipeline()
    for i in range(shard_level):
        shard_number = (i + shard_counter) % num_shards
        pipe.hget("shard", shard_number)

    write_shards_binary = pipe.execute()
    write_shards = list(map(lambda ws : ws.decode("utf-8"),write_shards_binary))
    message = {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": write_shards
    }
    return message
