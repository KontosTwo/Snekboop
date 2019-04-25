#Python CLI for Project Snekboop
#
#written by Chris Cale and Vincent Li

import sys
import os
import argparse
import boto3 #to access the aws api and the credentials (asuming they are already configured)

from os.path import expanduser #used to verify user directories
from botocore.exceptions import ClientError

class CLI:

	def __init__(self):
	        self.client = boto3.client('ec2')

	#CLI notes:
	#
	#functions we need:
		#def create(self): #--access=<access key> --secret=<secret key> --shard=<total number of partitions>
		#	print("hello")
		#	return "hello"

	#Creates an AWS Lamda service instance using either the preconfigured AWS credentials 
	#on local machine or allows the usr to specify the specific access key, and secret key.
	#Lasetly this takes in the number of AWS elasticache instances the user wants to 
	#distribute their data over.
	def create(self, access_key, secret_key, num_shards):
		print("create is correct")

		answer = self.existing_aws_user_credentials()
		#if file_exists(access_key):
		#	print("create_access_key     = " + str(access_key) )
		#if file_exists(access_key):
		#	print("create_secret_key    = " + str(secret_key) )

		#	print("create_num_shards     = " + str(num_shards) )
		print(answer)

	def deploy(self, deploy_handler_file):
		print("deploy is correct")

		#query that num_shards specified on cli is less than the var shard_level on the elasticache instance.

	def upload(self, upload_file_name, upload_num_shards, upload_jason_file):
		print("upload is correct")




	#helper functions below:

	#verification code:
	def file_exists( filename):
		print("got here")
		if os.path.isfile(filename):
			return True
		else:
			return False

	def verify_num_shards( num_shards):
		if num_shards > 0 and num_shards.is_integer():
			return True
		else:
			return False

	#verifies if the user already has credentials for AWS configured on local machine
	def existing_aws_user_credentials(self):
		#used: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-where
		#also referenced given code from assignment 1

		preconfigured_services = [] #use array because we might need to check more service configs 
		home_dir = expanduser("~")

		if os.path.exists(home_dir + "/.aws/credentials") and os.path.exists(home_dir + "/.aws/config"):
			preconfigured_services.append("aws")
        
		else:
			print("User's AWS credentials not found - initiating aws cli configuration")
			os.system("pip install awscli")
			os.system("aws configure")

		return preconfigured_services
		


def grab_args_from_cli():
	parser = argparse.ArgumentParser()
	parser.add_argument("snekboop", help="Sets up the infrastructure.")

	#sub commands under snekboop are create, deploy, and upload
	sub_parser = parser.add_subparsers(dest='sub_command')

	parser_create = sub_parser.add_parser('create')
	#source = https://stackoverflow.com/questions/36167685/how-to-pass-file-as-argument-in-python-script-using-argparse-module#36167749
	parser_create.add_argument('--access', action="store", dest='create_access_key', help="Path to AWS access key")
	parser_create.add_argument('--secret', action="store", dest='create_secret_key',help="Path to AWS secret key")
	parser_create.add_argument('--shard', type=int, dest='create_num_shards',default=1)


	parser_deploy = sub_parser.add_parser('deploy')
	parser_deploy.add_argument('--file', action="store", dest='deploy_handler_file', help="Path to Handler.zip")
	

	parser_upload = sub_parser.add_parser('upload')
	parser_upload.add_argument('--name', type=str, dest='upload_file_name', default=1)
	parser_upload.add_argument('--shard', type=int, dest='upload_num_shards',default=1)
	parser_upload.add_argument('--jason_file', action="store", dest='upload_jason_file', help="Path to .json file")


	args = parser.parse_args() #put into try catch and test later
	return args

def main():
	
	args = grab_args_from_cli()
	cli_handler = CLI()

    #testing that we can retireve all cli commands correctly
	print(args)
	print("\n==================================================\n")
	#create(self, access_key, secret_key, num_shards)


	if args.sub_command == 'create':
		cli_handler.create(args.create_access_key, args.create_secret_key, args.create_num_shards)

	elif args.sub_command == 'deploy':
		cli_handler.deploy(args.deploy_handler_file)

	elif args.sub_command == 'upload':
		cli_handler.upload(args.upload_file_name, args.upload_num_shards, args.upload_jason_file)



if __name__ == '__main__':
	    main()



