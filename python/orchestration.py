#!/usr/bin/env python

# this file will be used to run the necessary scripts to perform the following:
# 0. source openrc file --> could create one then source perhaps
# 1. check Swift container for files to process
# 2. boot instance, allocate floating ip
# 3. download files to be processed
# 4. run chosen pipeline on files
# 5. upload files back to Swift container
# 6. start whole process back over
import os, subprocess
from sys import argv
from time import sleep
from openstackfunctions import *
from runpipeline import run_json_commands

# constants for program
MAIN_DIRECTORY = '/home/cc/GenomicDoBox/'
BASH_DIRECTORY = MAIN_DIRECTORY + 'bash/'
JSON_DIRECTORY = MAIN_DIRECTORY + 'json/'
PYTHON_DIRECTORY = MAIN_DIRECTORY + 'python/'
REF_DIRECTORY = '/home/cc/ref_genome/'
CONTAINER = 'GenomicsStorage'
REF_FOLDER = 'RefGenome'
HG19_DIRECTORY = '/home/cc/hg19_database'
HG19_FOLDER = 'HG19Database'

print('Beginning implementation.')
# step 0: create, source openstack openrc file to access chameleon cloud --> needs to be completed
#os.system("export OS_PROJECT_INPUT=" + argv[1])
#os.system("export OS_USERNAME_INPUT=" + argv[2])
#os.system("export OS_PASSWORD_INPUT=" + "Parzival65536;")
#subprocess.call(JSON_DIRECTORY + "createopenrc.sh", shell=True)
#os.system("source /home/cc/openstack_docs/CH-818165.sh")
# step 1: check file_present function until it returns true
while not file_present(CONTAINER, "", "txt"):
	print('File type fastq still not present.')
	sleep(10)
# step 2: boot instance --> currently using boot.sh
# as of now, going to let the instance be this one
# step 3: download files to be processed
if download_files(CONTAINER, "", False):
	print('Download successful!')
# step 4: run chosen pipeline on files
# this requires the reference genome and snp_databases to be downloaded
# create function to check if these files exist in server, if not download them
if not os.listdir(REF_DIRECTORY):
	print('Reference Genome is not present. Need to download.')
	download_files(CONTAINER, REF_FOLDER, False)
if not os.listdir(HG19_DIRECTORY):
        print('HG19 database is not present. Need to download.')
        download_files(CONTAINER, HG19_FOLDER, False)
# prepare reference genome for use by calling prepareref.json
if run_pipeline_commands(JSON_DIRECTORY + 'prepareref.json'):
	print('Prepare reference genome was successful.')
