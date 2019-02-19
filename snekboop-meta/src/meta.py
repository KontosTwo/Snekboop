import json
import rpyc
import os
import boto3
import logging

logger = logging.getLogger()

meta_port = None
try:
    meta_port = os.environ["SNEKBOOP_META_PORT"]
except:
    logger.error("Failed initialization. The environment variable SNEKBOOP_META_PORT must be defined")
    exit(1)

access_key = None
try:
    access_key = os.environ["AWS_ACCESS_KEY_ID"]
except:
    logger.error("Failed initialization. The environment variable AWS_ACCESS_KEY_ID must be defined")
    exit(1)

secret_key = None
try:
    secret_key = os.environ["AWS_SECRET_ACCESS_KEY"]
except:
    logger.error("Failed initialization. The environment variable AWS_SECRET_ACCESS_KEY must be defined")
    exit(1)


session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
)
client = session.client('ec2', region_name='us-west-2')

class MetaService(rpyc.Service):
    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass

def init():
    response = client.create_security_group(GroupName='SECURITY_GROUP_NAME',
                                         Description='DESCRIPTION',
                                         VpcId=vpc_id)

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MetaService, port=int(meta_port))
    t.start()
