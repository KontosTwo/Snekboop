from rpyc import *
from uhashring import HashRing
import string
import os

port = None

try:
    port = os.environ["SNEKBOOP_HUB_PORT"]
except:
    print("Failed initialization. The environment variable SNEKBOOP_HUB_PORT must be defined")


class HubService(Service):

    def __init__(self):
        self.hash_ring = HashRing(nodes=[])

    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def write(self, name, data):
        for index, datum in enumerate(data):
            print(name + str(datum))


if __name__ == "__main__":
    t = ThreadedServer(HubService, port=int(port))
    t.start()
