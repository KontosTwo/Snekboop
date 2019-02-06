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

    def exposed_write(self, name, data):
        pass


if __name__ == "__main__":
    t = ThreadedServer(HubService, port=int(port))
    t.start()
