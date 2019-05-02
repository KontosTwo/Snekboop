#this class has the wrappers for api calls

import os
import json
import requests

#stating all the urls we need
write_url="https://wnn3cmovfc.execute-api.us-west-2.amazonaws.com/default/Write"

query_url="https://wnn3cmovfc.execute-api.us-west-2.amazonaws.com/default/Query"

add_function_url="https://xievn5u85f.execute-api.us-west-2.amazonaws.com/default/AddFunction"

upload_url="???"





def query_call(name, function):
    json_data = {
        "name" : name,
        "function" : function
    }
    headers = {
        "Content-Type" : "application/json"
    }
    return requests.post(url=query_url,data=json.dumps(json_data), headers=headers).json()["body"]


def write_call(name, data):
    json_data = {
        "name": name,
        "data": data
    }
    requests.post(url=query_url,data=json.dumps(json_data)).json()


































