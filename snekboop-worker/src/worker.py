import redis
import json
import rpyc
import os
import asyncio

worker_port = None

try:
    worker_port = os.environ["SNEKBOOP_WORKER_PORT"]
except:
    print("Failed initialization. The environment variable SNEKBOOP_WORKER_PORT must be defined")
    exit(1)

access_key = None

try:
    access_key = os.environ["AWS_ACCESS_KEY_ID"]
except:
    print("Failed initialization. The environment variable AWS_ACCESS_KEY_ID must be defined")
    exit(1)

secret_key = None

try:
    secret_key = os.environ["AWS_SECRET_ACCESS_KEY"]
except:
    print("Failed initialization. The environment variable AWS_SECRET_ACCESS_KEY must be defined")
    exit(1)

redis_host = None

try:
    redis_host = os.environ["REDIS_HOST"]
except:
    print("Failed initialization. The environment variable REDIS_HOST must be defined")
    exit(1)

redis_port = None

try:
    redis_port = os.environ["REDIS_PORT"]
except:
    print("Failed initialization. The environment variable REDIS_PORT must be defined")
    exit(1)

r = redis.Redis(host=redis_host, port=redis_port, db=0)


class WorkerService(rpyc.Service):
    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

    def exposed_write(self, name, data):
        r.execute_command('JSON.ARRAPPEND', name, '.', data)
        pass

    def exposed_query(self, name, func):
        json_list = json.loads(r.execute_command('JSON.GET', name))
        self.process_queries(json_list, func)
        pass

    async def process_queries(self, json_list, func):
        loop = asyncio.get_event_loop()
        futures = []
        for json_object in json_list:
            futures.append(func(json_object))
        results = loop.run_until_complete(asyncio.gather(futures))
        return results

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(WorkerService, port=int(worker_port))
    t.start()
