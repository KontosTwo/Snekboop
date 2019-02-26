import rpyc
import os
import boto3
import multiprocessing

port = None
try:
    port = int(os.environ['SNEKBOOP_WORKER_PORT'])
except Exception as e:
    print("SNEKBOOP_WORKER_PORT not set")

access_key = None
try:
    access_key = os.environ['SNEKBOOP_ACCESS_KEY']
except Exception as e:
    print("SNEKBOOP_ACCESS_KEY not set")

secret_key = None
try:
    secret_key = os.environ['SNEKBOOP_SECRET_KEY']
except Exception as e:
    print("SNEKBOOP_SECRET_KEY not set")


session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
)

s3 = session.resource('s3')

class WorkerService(rpyc.Service):

    def __init__(self):
        self.data = {}

    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_write(self, name, data):
        data[name].append(data)
        pass

    def exposed_query(self, name, bucket, path):
        pass


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(WorkerService, port=port)
    t.start()
