from flask import Flask, request
from flask_restful import Resource, Api
import rpyc
import os
import sys

hub_port = None

try:
    hub_port = os.environ["SNEKBOOP_HUB_PORT"]
except:
    print("Failed initialization. The environment variable SNEKBOOP_HUB_PORT must be defined")

hub_ip = None

try:
    hub_ip = os.environ["SNEKBOOP_HUB_IP"]
except:
    print("Failed initialization. The environment variable SNEKBOOP_HUB_IP must be defined")

api_port = None

try:
    api_port = os.environ["SNEKBOOP_API_PORT"]
except:
    print("Failed initialization. The environment variable SNEKBOOP_API_PORT must be defined")

app = Flask(__name__)
api = Api(app)


hub_connection = rpyc.connect(hub_ip, hub_port)


class SnekboopAPI(Resource):
    def post(self, name):
        json_data = request.get_json(force=True)
        hub_connection.root.write(name, json_data["data"])
        return {"message": "success"}, 201


api.add_resource(SnekboopAPI, '/<string:name>/write')


if __name__ == '__main__':
    app.run(debug=True, port=api_port)
