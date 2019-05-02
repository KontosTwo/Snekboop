#this class has the wrappers for api calls

import os
import json
import requests

#stating all the urls we need
write_url="https://wnn3cmovfc.execute-api.us-west-2.amazonaws.com/default/Write"

query_url="https://wnn3cmovfc.execute-api.us-west-2.amazonaws.com/default/Query"

add_function_url="https://xievn5u85f.execute-api.us-west-2.amazonaws.com/default/AddFunction"

upload_url="???"




class api_calls:

    def query_call(func, parameters, json_item):
        return requests.post(url=query_url,json=post_json,params=parameters).json()[json_item]
         

    def upload_call(func, url, json_item):
        return requests.post(url=upload_url,json=post_json,params=parameters).json()[json_item]


    def write_call(func, url, json_item):
        return requests.post(url=write_url,json=post_json,params=parameters).json()[json_item]

    def add_function_call(func, url, json_item):
        return requests.post(url=add_function_url,json=post_json,params=parameters).json()[json_item]


if __name__ == '__main__':
     app.run(port='5000') #check that this port will work



































