from rpyc import *
import string
import os

num_child_nodes = None
port = None

try:
    num_child_nodes = os.environ["SNEKBOOP_NUM_CHILDREN_NODES"]
except:
    print("Failed initialization. The environment variable SNEKBOOP_NUM_CHILDREN_NODES must be defined")

try:
    port = os.environ["SNEKBOOP_PORT"]
except:
    print("Failed initialization. The environment variable SNEKBOOP_PORT must be defined")


class HubService(Service):
    def on_connect(self, conn: Connection):
        conn.
        pass

    def on_disconnect(self, conn: Connection):
        pass

    def write(self, name: string, data: list[dict]):
        for index, datum in enumerate(data):
            shard_number = index % num_child_nodes
