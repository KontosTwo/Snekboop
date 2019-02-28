import rpyc
import os
import boto3
import importlib

port = None
try:
    port = int(os.environ['SNEKBOOP_LB_PORT'])
except Exception as e:
    print("SNEKBOOP_LB_PORT not set")

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


class LoadBalancerService(rpyc.Service):

    def __init__(self):
        self.functions = {}
        self.virtual_workers = []

    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_connect(self, virtual_worker_host, virtual_worker_post):
        self.virtual_workers.append(VirtualWorkerAddress(virtual_worker_host, virtual_worker_post))

    def exposed_write(self, name, data):
        pass

    def exposed_query(self, name, bucket, key):
        function = self.__fetch_function(bucket, key)
        pass

    def __fetch_function(self, bucket, key):
        func_id = bucket + key
        if func_id in self.functions:
            return self.functions[func_id]
        else:
            func_file_name = func_id + '.py'
            s3.Bucket(bucket).download_file(key, func_file_name)


            return self.functions[func_id]


    def __chunks(self, l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]


class VirtualWorkerAddress:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def conn(self):
        return rpyc.connect(self.host, self.port)


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(LoadBalancerService(), port=port)
    t.start()
