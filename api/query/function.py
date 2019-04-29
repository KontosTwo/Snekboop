import os
import json
import requests
import aioredis
import asyncio

def handler(event, context):
    loop = asyncio.get_event_loop()

    meta_find_url = os.environ["META_FIND_URL"]

    name = event["name"]
    data = event["data"]

    post_json ={
        "name": name
    }
    params = {
        "Content-Type" : "application/json"
    }
    shards = requests.post(url=meta_find_url,json=post_json,params=params).json()["body"]
    loop.run_until_complete(write_job(loop, name, shards, data))

    message = {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": "Successfully written to snekboop"
    }
    return message

async def write_job(loop,name, shards,data):
    write_promises = []
    conns = []
    conn_close_promises = []
    for shard in shards:
        shard_dict = json.loads(shard)
        conn = await aioredis.create_redis(
            (shard_dict["host"], shard_dict["port"]))
        multi = conn.multi_exec()
        for datum in data:
            multi.lpush(name,json.dumps(datum))
        conns.append(conn)
        write_promises.append(multi.execute())

    for write_promise in write_promises:
        await write_promise

    for conn in conns:
        conn.close()