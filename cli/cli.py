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
def create(access_key, secret_key, num_shards):
	print("create is correct")

	if file_exists(access_key):
		print("create_access_key     = " + str(access_key) )
		print("create_secret_key    = " + str(secret_key) )
		print("create_num_shards     = " + str(num_shards) )


def deploy(deploy_handler_file):
	print("deploy is correct")


def upload(upload_file_name, upload_num_shards, upload_jason_file):
	print("upload is correct")






#verification code:
def file_exists( filename):
	print("got here")
	#if os.path.exists(filename)
	#	return True
	#else
	#	return False
	return True




def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("snekboop", help="Sets up the infrastructure.")

	#sub commands under snekboop are create, deploy, and upload
	sub_parser = parser.add_subparsers(dest='sub_command')

	parser_create = sub_parser.add_parser('create')
	#source = https://stackoverflow.com/questions/36167685/how-to-pass-file-as-argument-in-python-script-using-argparse-module#36167749
	parser_create.add_argument('-access', action="store", dest='create_access_key', help="Path to AWS access key")
	parser_create.add_argument('-secret', action="store", dest='create_secret_key',help="Path to AWS secret key")
	parser_create.add_argument('-shard', type=int, dest='create_num_shards',default=1)


	parser_deploy = sub_parser.add_parser('deploy')
	parser_deploy.add_argument('-file', action="store", dest='deploy_handler_file', help="Path to Handler.zip")
	

	parser_upload = sub_parser.add_parser('upload')
	parser_upload.add_argument('-name', type=str, dest='upload_file_name', default=1)
	parser_upload.add_argument('-shard', type=int, dest='upload_num_shards',default=1)
	parser_upload.add_argument('-jason_file', action="store", dest='upload_jason_file', help="Path to .json file")

	#parse all commands together from cli
	#try:
    #    args = parser.parse_args()
    #except IOError, msg:
    #    parser.error(str(msg))

	args = parser.parse_args()


    #testing that we can retireve all cli commands correctly
	print(args)
	print("\n==================================================\n")
	#create(self, access_key, secret_key, num_shards)


	if args.sub_command == 'create':
		create(args.create_access_key, args.create_secret_key, args.create_num_shards)

	elif args.sub_command == 'deploy':
		deploy(args.deploy_handler_file)

	elif args.sub_command == 'upload':
		upload(args.upload_file_name, args.upload_num_shards, args.upload_jason_file)



if __name__ == '__main__':
    main()



