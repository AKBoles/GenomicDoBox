#!/usr/bin/env python

# TO DO: CHANGE DIRECTORY NAMES TO MATCH SWIFT CONTAINER!!!

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
import openstackfunctions as osf
import runpipeline as runp

# constants for program
MAIN_DIRECTORY = '/home/cc/GenomicDoBox/'
BASH_DIRECTORY = MAIN_DIRECTORY + 'bash/'
JSON_DIRECTORY = MAIN_DIRECTORY + 'json/'
PYTHON_DIRECTORY = MAIN_DIRECTORY + 'python/'
REF_DIRECTORY = '/home/cc/RefData/'
CONTAINER = 'GenomicsStorage'
REF_FOLDER = 'ReferenceData'
HG19_DIRECTORY = '/home/cc/HG19Data'
HG19_FOLDER = 'HG19Data'
DATA_DIRECTORY = '/home/cc/data_processing/to_be_processed'
TO_BE_PROCESSED = 'to_be_processed'

def chdir(dest):
	old = os.getcwd()
	os.chdir(dest)
	new = os.getcwd()
	print('old: %s, new: %s' %(old, new))

def prepref(logfile):
	# prepare reference genome for use by calling prepareref.json
	if runp.runjsoncommands(JSON_DIRECTORY + 'prepareref.json', logfile):
        	print('Preparing Reference Genome was successful.')

def checkref(logfile):
	# first check for hg19 database:
	if not os.listdir(HG19_DIRECTORY):
		chdir(HG19_DIRECTORY)
		print('HG19 database is not present. Need to download.')
		osf.downloadfiles(CONTAINER, HG19_FOLDER, False)
	else:
		print('HG19 database is already present in server!')
	if not os.listdir(REF_DIRECTORY):
		chdir(REF_DIRECTORY)
		print('Reference Genome is not present. Need to download.')
		osf.downloadfiles(CONTAINER, REF_FOLDER, False)
	elif len(os.listdir(REF_DIRECTORY)) is 1:
		chdir(REF_DIRECTORY)
		print('Reference Genome is downloaded but needs to be prepared -- beginning process.')
		prepref(logfile)
	else:
		print('Reference Genome is already present in server and prepared!')
	return True

print('Beginning implementation.')
logfile = open('logfile.txt', 'w')
# step 0: create, source openstack openrc file to access chameleon cloud --> needs to be completed
# step 1: check file_present function until it returns true
while not osf.filepresent(CONTAINER, TO_BE_PROCESSED, "fastq"):
	print('File type fastq still not present.')
	sleep(10)
# step 2: boot instance --> currently using boot.sh
# as of now, going to let the instance be this one
# step 3: download files to be processed
# change directory to 'data_processing/to_be_processed'
chdir('/home/cc/data_processing')
if not os.listdir(DATA_DIRECTORY):
	print('FASTQ files need to be downloaded.')
	if osf.downloadfiles(CONTAINER, TO_BE_PROCESSED, False):
		print('Download successful!')
else:
	print('There are already files ready for processing!')
# step 4: run chosen pipeline on files
# this requires the reference genome and snp_databases to be downloaded / prepared
if checkref(logfile):
	print('The database and reference genome were downloaded and prepared.')
# now to run the chosen pipeline --> currently just running sample.json in json folder
#chdir('/home/cc/data_processing/to_be_processed')
#if runp.runjsoncommands(JSON_DIRECTORY + argv[1], logfile):
#	print('Running %s was successful!' %argv[1])

# once the process is done, close logfile
logfile.close()
