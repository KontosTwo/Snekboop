import os
import json
import aioredis
import asyncio
import requests
import aiohttp


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
    async with aiohttp.ClientSession() as session:
        for shard in shards:
            shard_dict = json.loads(shard)
            conn = await aioredis.create_redis(
                (shard_dict["host"], shard_dict["port"]))
            data = await conn.lrange(name, 0, -1)
            post_json = {
                "data": list(map(lambda d: d.decode("utf-8").strip('"'), data))
            }
            print(post_json)
            headers = {
                "Content-Type": "application/json",

                "Accept": "application/json"
            }
            result = process_data(session, function_url,json.dumps(post_json),headers)
            conns.append(conn)
            results.append(result)

        for result in results:
            print(await result)

        for conn in conns:
            conn.close()

    return final_result

async def process_data(session, url, data, headers):
    async with session.post(url, data=data, headers=headers) as response:
        return await response.read()
