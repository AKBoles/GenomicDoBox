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
import os, subprocess, sys
from sys import argv
from time import sleep
import openstackfunctions as osf
import runpipeline as runp
import basicfunctions as basic

# constants for program
# RENAME CONSTANTS!!!
REF_DIRECTORY = '/home/cc/RefData/'
JSON_DIRECTORY = '/home/cc/GenomicDoBox/json/'
CONTAINER = 'GenomicsStorage'
TEST_CONTAINER = 'GenomicDoBox'
REF_FOLDER = 'ReferenceData'
HG19_DIRECTORY = '/home/cc/HG19Data'
HG19_FOLDER = 'HG19Data'
DATA_DIRECTORY = '/home/cc/DataProcessing'
TO_BE_PROCESSED = 'ToBeProcessed'
DOWNLOAD_DIRECTORY = '/home/cc/Downloads'
UPLOAD_DIRECTORY = '/home/cc/Uploads'
PROCESS_DIRECTORY = '/home/cc/DataProcessing'

print('Beginning implementation.')
# step 0: create, source openstack openrc file to access chameleon cloud --> needs to be completed
#	need to look into 

# step 1: obtain, index the reference genome and snp_databases
logfile = open('log.txt', 'w')
if basic.checkref(logfile):
	# this check sto see if the references are downloaded and prepared
        print('The database and reference genome were downloaded and prepared.')

# step 2: check file_present function until it returns true
while not osf.filepresent(TEST_CONTAINER, TO_BE_PROCESSED, "fastq"):
	print('File type fastq still not present.')
	sleep(10)

# step 3: boot instance --> currently using boot.sh
# as of now, going to let the instance be this one

# step 4: download files to be processed
# first download to Downloads folder then move
basic.chdir(DOWNLOAD_DIRECTORY)
if not os.listdir(DATA_DIRECTORY):
	print('FASTQ files need to be downloaded.')
	if osf.downloadfiles(TEST_CONTAINER, TO_BE_PROCESSED, False):
		print('Download successful!')
else:
	# make sure that this also puts it in processing folder
	# where does it put them if this is the case? --> will not worry now
	print('There are already files ready for processing!')
# step 5: run chosen pipeline on files
# now to run the chosen pipeline --> currently just running sample.json in json folder
basic.chdir(DATA_DIRECTORY)
if basic.movefastq('test'):
	print('Moved fastq files, now to start the chosen pipeline.')
basic.chdir(DATA_DIRECTORY)
if runp.runjsoncommands(JSON_DIRECTORY + argv[1], logfile):
	# need to get rid of argv use!!
	print('Running %s was successful!' %argv[1])

# next: upload the files to PostProcessing in Swift
# move to Uploads file
if basic.movefile('final.bam', '/home/cc/Uploads/test_final.bam'):
	print('Moved, renamed final file to Uploads file...now to upload back to swift.')
basic.chdir(UPLOAD_DIRECTORY)
if osf.uploadfiles(TEST_CONTAINER + '/PostProcessing', '', ['test_final.bam']):
	print('Uploaded files correctly!')

# next: delete files from the instance to prepare for another two files
if basic.deletefiles():
	print('Files deleted from the instance. Ready for another file to process!')

# finally, before ready to restart the script, need to delete files from ToBeProcessed in swift container
# for now skipping this to test restart

# restart the script!
basic.chdir('/home/cc/GenomicDoBox/python')
os.execv(sys.executable, ['python'] + sys.argv)

# once the process is done, close logfile
logfile.close()
