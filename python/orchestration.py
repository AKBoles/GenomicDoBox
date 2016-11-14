#!/usr/bin/env python

######################################
#
# this file will be used to run the necessary scripts to perform the following:
# 0. source openrc file --> needs to be done 
# 1. check Swift container for files to process --> done!
# 2. boot instance, allocate floating ip --> needs to be done
# 3. download files to be processed --> done!
#	a. Needs to be placed in correct directories on instance --> done!
# 4. run chosen pipeline on files --> done!
#	a. Allow users to choose what pipeline to run --> needs to be done
# 5. upload files back to Swift container --> done!
# 6. start whole process back over --> done!
#	a. Needs for everything to be reset so that new files can be processed
#
######################################

# import statements
import os, subprocess, sys
from sys import argv
from time import sleep
import openstackfunctions as osf
import runpipeline as runp
import basicfunctions as basic

print('Beginning implementation.')
sys.stdout = open('test_log.txt', 'w')
# step 0: create, source openstack openrc file to access chameleon cloud --> needs to be completed
#	need to look into 

# step 1: obtain, index the reference genome and snp_databases
logfile = open('log.txt', 'w')
if basic.checkref(logfile):
	# this check sto see if the references are downloaded and prepared
        print('The database and reference genome were downloaded and prepared.')

# step 2: check file_present function until it returns true
while not osf.filepresent(basic.TEST_CONTAINER, basic.TO_BE_PROCESSED, "fastq"):
	print('File type fastq still not present.')
	sleep(10)

# step 3: boot instance --> currently using boot.sh
# as of now, going to let the instance be this one

# step 4: download files to be processed
# first download to Downloads folder then move
basic.chdir(basic.DOWNLOAD_DIRECTORY)
if not os.listdir(basic.DATA_DIRECTORY):
	print('FASTQ files need to be downloaded.')
	if osf.downloadfiles(basic.TEST_CONTAINER, basic.TO_BE_PROCESSED):
		print('Download successful!')
else:
	# make sure that this also puts it in processing folder
	# where does it put them if this is the case? --> will not worry now
	print('There are already files ready for processing!')
# step 5: run chosen pipeline on files
# now to run the chosen pipeline --> currently just running sample.json in json folder
basic.chdir(basic.DATA_DIRECTORY)
# need to fix this! need to be able to grab initial fastq name and store it for later use
# currently hardcoded! --> not good
if basic.movefastq('test'):
	print('Moved fastq files, now to start the chosen pipeline.')
basic.chdir(basic.DATA_DIRECTORY)
if runp.runjsoncommands(basic.JSON_DIRECTORY + argv[1], logfile):
	# need to get rid of argv use!!
	print('Running %s was successful!' %argv[1])

# next: upload the files to PostProcessing in Swift
# move to Uploads file
# undo these! (FIX!!) --> needs to not be hardcoded
if basic.movefile('final.bam', '/home/cc/Uploads/test_final.bam'):
	print('Moved, renamed final file to Uploads file...now to upload back to swift.')
basic.chdir(basic.UPLOAD_DIRECTORY)
if osf.uploadfiles(basic.TEST_CONTAINER + '/PostProcessing', '', ['test_final.bam']):
	print('Uploaded files correctly!')

# next: delete files from the instance to prepare for another two files
if basic.deletefiles():
	print('Files deleted from the instance. Ready for another file to process!')

# finally, before ready to restart the script, need to delete files from ToBeProcessed in swift container
# for now skipping this to test restart

basic.chdir(basic.PYTHON_DIRECTORY)

sys.stdout.close()
# upload the log to swift storage
if osf.uploadfiles(basic.TEST_CONTAINER + '/PostProcessing', '', ['test_log.txt']):
        print('Log files uploaded successfully.')

# restart the script!
#os.execv(sys.executable, ['python'] + sys.argv)

# once the process is done, close logfile
logfile.close()
