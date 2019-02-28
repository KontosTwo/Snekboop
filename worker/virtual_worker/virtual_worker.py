import rpyc
import os
import boto3
import socket
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

lb_host = None
try:
    lb_host = os.environ['SNEKBOOP_LB_HOST']
except Exception as e:
    print("SNEKBOOP_LB_HOST not set")

lb_port = None
try:
    lb_port = int(os.environ['SNEKBOOP_LB_PORT'])
except Exception as e:
    print("SNEKBOOP_LB_PORT not set")

session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
)

s3 = session.resource('s3')

class WorkerService(rpyc.Service):

    def __init__(self):
        self.data = {}
        self.host = socket.gethostname()
        self.port = port
        lb_conn = rpyc.connect(lb_host, lb_port)
        lb_conn.root.connect(self.host, self.port)


    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_write(self, name, data):
        data[name].extend(data)
        pass

    def exposed_execute(self, name, func):
        data_list = self.data[name]
        return func(data_list)


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(WorkerService(), port=port)
    t.start()
