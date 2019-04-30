import os
import json
import aioredis
import asyncio
import requests
import requests_async


def handler(event, context):
    loop = asyncio.get_event_loop()

    meta_find_url = os.environ["META_FIND_URL"]
    meta_find_function_url = os.environ["META_FIND_FUNCTION_URL"]

    name = event["name"]
    function = event["function"]

    post_json = {
        "name": name
    }
    params = {
        "Content-Type": "application/json"
    }
    shards = requests.post(url=meta_find_url, json=post_json, params=params).json()["body"]

    post_json2 = {
        "func_name": function
    }
    params2 = {
        "Content-Type": "application/json"
    }
    response = requests.post(url=meta_find_function_url, json=post_json2, params=params2).json()
    function_url = response['body']

    data = loop.run_until_complete(query_job(loop, name, shards, function_url))

    message = {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(data)
    }
    return message


async def query_job(loop, name, shards, function_url):
    conns = []
    results = []
    final_result = []

    for shard in shards:
        shard_dict = json.loads(shard)
        conn = await aioredis.create_redis(
            (shard_dict["host"], shard_dict["port"]))
        data = await conn.lrange(name, 0, -1)

        post_json = {
            "data": data
        }
        params = {
            "Content-Type": "application/json"
        }
        result = requests_async.post(url=function_url, json=post_json, params=params)
        conns.append(conn)
        results.append(result)

    for result in results:
        print(result)

    for conn in conns:
        conn.close()

    return final_result