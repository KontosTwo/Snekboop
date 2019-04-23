import os
import redis
import json
import requests

def handler(event, context):
    meta_find_url = os.environ["META_FIND_URL"]

    name = event["name"]
    data = event["data"]
    data_length = len(data)

    body ={
        "name": name
    }
    shards = requests.get(url=meta_find_url,data=body).json()



    message = {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": "Successfully written to snekboop " + str(shards)
    }
    return message
