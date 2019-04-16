#Python CLI for Project Snekboop
#
#written by Chris Cale and Vincent Li

import sys
import os
import argparse



#class cli:

#CLI notes:
#
#functions we need:
	#def create(self): #--access=<access key> --secret=<secret key> --shard=<total number of partitions>
	#	print("hello")
	#	return "hello"
	#create --access=<access key> --secret=<secret key> --shard=<total number of partitions>

	#deploys node.js landa deployment package
	#def deploy(self):# <handler>.zip



	#def upload(self):# --name=<name of category> --shard=<number of partitions> <json-file>.json
	 

	#Library - Implement in python, using asyncio https://stackoverflow.com/questions/22190403/how-could-i-use-requests-in-asyncio

	#def write(name, json):


	#def query(name, query): 






def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("create", help="Sets up the infrastructure.")
	parser.add_argument("deploy", help="Programmatically deploys a node.")
	parser.add_argument("upload", help="Uploads a json list of data to the system.")
	parser.add_argument("write", help="Fetches authentication info from environment variables.")
	parser.add_argument("query", help="Fetches authentication info from environment variables.")
	args = parser.parse_args()
	
	#args = parser.parse_args()
	#if(args.create):
	#	print("args = create")
	#elif(args.deploy):
	#	print("args = deploy")
	#elif(args.upload):
	#	print("args = upload")
	#elif(args.write):
	#	print("args = write")
	#elif(args.query):
	#	print("args = query")

    #my_cli = cli()

    #referenced: https://docs.python.org/2/howto/argparse.html
    #parser = argparse.ArgumentParser()


    
	print(args.create)
	#
    # code here


    #while True:
    #	try:
    #		cli_string = ''

#	except Exception as e:
#   		print(e)


if __name__ == '__main__':
    main()



