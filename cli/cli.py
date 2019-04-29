#Python CLI for Project Snekboop
#
#written by Chris Cale and Vincent Li

import sys
import os
import argparse
import boto3 #to access the aws api and the credentials (asuming they are already configured)
import json #for parsing and interacting with the json data

from os.path import expanduser #used to verify user directories
from botocore.exceptions import ClientError
from pathlib import Path #used to convert strings to Path types

class CLI:

	#class objects stored for global reference
	shard_level = 0 #defaults to 0 when CLI is initially run.
	local_upload_filename_store = {}


	def __init__(self):
	        self.client = boto3.client('ec2') #!!! discuss using a session instead of a client

	#Creates an AWS Lamda service instance using either the preconfigured AWS credentials 
	#on local machine or allows the usr to specify the specific access key, and secret key.
	#Lasetly this takes in the number of AWS elasticache instances the user wants to 
	#distribute their data over.
	def create(self, access_key, secret_key, num_shards):
		print("create is correct")

		#check if aws credentials exist
		existing_credentials = self.existing_aws_user_credentials()

		#if either key is specified then overwrite that key
		if self.file_exists(access_key) and access_key is  None:
			print("create_access_key     = " + str(access_key) )
		if self.file_exists(secret_key) and secret_key is  None:
			print("create_secret_key    = " + str(secret_key) )

		#verify shard value
		if self.verify_num_shards(num_shards):
			print("create_num_shards     = " + str(num_shards) )
			self.shard_level = num_shards
			print("self.shard_level     = " + str(self.shard_level) )

		
		print(existing_credentials)



	def deploy(self, deploy_handler_file):
		print("deploy is correct")

		#query that num_shards specified on cli is less than the var shard_level on the elasticache instance.

	def upload(self, upload_file_name, upload_num_shards, upload_jason_file):
		print("upload is correct")

		#upload_file_name -> make sure that it is a unique name -> perhaps use a quick 
		#lookup table which is stored locally?


		if self.file_exists( input_file):
			self.get_num_json_records(upload_file_name)



	#helper functions below:

	#Returns True if the specified Upload_filename was successfully uploaded.
	def add_upload_filename_to_local_store(self, filename):
		add_check = len(local_upload_filename_store)
		if filename is not None
			if filename in local_upload_filename_store:
				print("TESTING: This upload_filename already exists")
			else:
				local_upload_filename_store[str(filename)] = str(filename) #may need to rethink this datastructure, or perhaps store something other than the name as the value

		if len(local_upload_filename_store) > add_check
			return True
		else:
			return False

	#Returns True if the specified Upload_filename was successfully removed.
	def remove_upload_filename_from_local_store(self, filename):
		remove_check = len(local_upload_filename_store)
		if filename is not None
			if filename in local_upload_filename_store:
				print("TESTING: This upload_filename is in the local store")
				local_upload_filename_store.pop(str(filename))
			else:
				print("TESTING: this filename does not exist")

		if len(local_upload_filename_store) < remove_check
			return True
		else:
			return False

	#Returns True if entire dictionary was successfully deleted.
	def delete_entire_upload_filemane_local_store(self):
		if len(local_upload_filename_store) is not 0
			del local_upload_filename_store

		return len(local_upload_filename_store) == 0


	#Provides standard error messages to other CLI functions.
	def print_error(self, issue):
		#referenced assignment 2 for intuitive error handling
		built_in_error_messages = {}

		#for create function
		built_in_error_messages['incorrect_shard_value'] = 'The shard value must be an integer value greater than 0.'

		#for when the file does not exist in the filesystem
		built_in_error_messages['file_does_not_exist'] = 'The specified file does not exist.'

		#if issue does not have an error message:
		built_in_error_messages['unknown_error'] = 'Something was not correct with the request. Try again.'
		
		if issue:
			return built_in_error_messages[issue]
		else:
			return built_in_error_messages['unknown_error']


	#Verifies that the input filen actually exists - the contents of the file will not be checked.
	def file_exists(self, filename):
		print("entered func file_exists\n")
		path_to_verify = Path(str(filename))
		if os.path.isfile(path_to_verify):
			return True
		else:
			print( self.print_error('file_does_not_exist') ) 
			return False

	#Verifies that the input number of shards is positive and at least 1.
	def verify_num_shards(self, num_shards):
		print("entered func verify_num_shards\n")

		if num_shards > 0:
			return True
		else:
			print( self.print_error('incorrect_shard_value') )
			return False

	#verifies if the user already has credentials for AWS configured on local machine
	def existing_aws_user_credentials(self):
		#used: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-where
		#also referenced given code from assignment 1

		#default action if keys are not specified is to grab the preconfigured aws account credentials
		#but we need to discuss if we need to use a boto3.session instead of boto3.client
		preconfigured_services = [] #use array because we might need to check more service configs 
		home_dir = expanduser("~")

		if os.path.exists(home_dir + "/.aws/credentials") and os.path.exists(home_dir + "/.aws/config"):
			preconfigured_services.append("aws")
        
		else:
			print("User's AWS credentials not found - initiating aws cli configuration")
			os.system("pip install awscli")
			os.system("aws configure")

		return preconfigured_services
		
	#Returns number of json records in a file. 
	def get_num_json_records(self, input_file):
		print("Entered get_num_json_records()")
		count = 0
		if self.file_exists( input_file):
			print("TEST_TEST_TEST")
			#records = json.load(input_file)
			#long for-loop method - may want to change later see comment below
			#for record in records
			#	count++

		return count

		#note: research indicates that we could use json.loads() function to easily grab all the 
		#json elements into a dictionary and then use len(json_dictionary_var_name) to quickly
		#get the number of elements, but we must know the json structure first
		#
		#I will assume a basic sturcture of top level "records" and then many "record" 
		#within that structure - see test.json in this folder

		


#non-CLI class functions
def grab_args_from_cli():
	#referenced for argparse tutorial: https://rajadavidhasugian.wordpress.com/2017/06/10/using-argparse-to-pass-arguments-into-python-script/
	#referenced for argparse FileType syntax = https://stackoverflow.com/questions/36167685/how-to-pass-file-as-argument-in-python-script-using-argparse-module#36167749

	parser = argparse.ArgumentParser()
	parser.add_argument("snekboop", help="Sets up the infrastructure.")

	#sub commands under snekboop are create, deploy, and upload
	sub_parser = parser.add_subparsers(dest='sub_command')

	parser_create = sub_parser.add_parser('create')
	parser_create.add_argument('--access', action="store", dest='create_access_key', help="Path to AWS access key")
	parser_create.add_argument('--secret', action="store", dest='create_secret_key',help="Path to AWS secret key")
	parser_create.add_argument('--shard', type=int, dest='create_num_shards',default=1)

	parser_deploy = sub_parser.add_parser('deploy')
	parser_deploy.add_argument('--file', action="store", dest='deploy_handler_file', help="Path to Handler.zip")
	
	parser_upload = sub_parser.add_parser('upload')
	parser_upload.add_argument('--name', type=str, dest='upload_file_name')
	parser_upload.add_argument('--shard', type=int, dest='upload_num_shards',default=1)
	parser_upload.add_argument('--jason_file', action="store", dest='upload_jason_file', help="Path to .json file")

	args = None
	try:
		args = parser.parse_args()
	except Exception as e:
		print(e)

	return args



def main():
	
	args = grab_args_from_cli()
	cli_handler = CLI()

    #testing that we can retireve all cli commands correctly
	print(args)
	print("\n==================================================\n")


	if args.sub_command == 'create':
		cli_handler.create(args.create_access_key, args.create_secret_key, args.create_num_shards)

	elif args.sub_command == 'deploy':
		cli_handler.deploy(args.deploy_handler_file)

	elif args.sub_command == 'upload':
		cli_handler.upload(args.upload_file_name, args.upload_num_shards, args.upload_jason_file)



if __name__ == '__main__':
	    main()



