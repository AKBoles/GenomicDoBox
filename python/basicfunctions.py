import os, sys, re, json, time
import collections
import openstackfunctions as osf
import runpipeline as runp

# constants for program
# do not really want these in both directories
MAIN_DIRECTORY = '/home/cc/GenomicDoBox/'
BASH_DIRECTORY = MAIN_DIRECTORY + 'bash/'
JSON_DIRECTORY = MAIN_DIRECTORY + 'json/'
PYTHON_DIRECTORY = MAIN_DIRECTORY + 'python/'
REF_DIRECTORY = '/home/cc/RefData/'
CONTAINER = 'GenomicsStorage'
REF_FOLDER = 'ReferenceData'
HG19_DIRECTORY = '/home/cc/HG19Data'
HG19_FOLDER = 'HG19Data'
DATA_DIRECTORY = '/home/cc/DataProcessing'
TO_BE_PROCESSED = 'ToBeProcessed'
DOWNLOAD_DIRECTORY = '/home/cc/Downloads'

def chdir(dest):
        old = os.getcwd()
        os.chdir(dest)
        new = os.getcwd()
        print('old: %s, new: %s' %(old, new))

def writedir(path, name):
	# given a path and name of directory, create it
	# make sure to return to original directory
	orig = os.getcwd()
	os.chdir(path)
	print('Original directory: %s ; New Directory: %s' %(orig, os.getcwd()))
	os.mkdir(name, 0755)
	print('Created new directory at: %s' %(path + name))
	os.chdir(orig)
	return True

def movefile(name, newname):
	os.rename(name, newname)

def movefastq(name):
	# set up new R1, R2 names:
	chdir(DOWNLOAD_DIRECTORY)
	R1 = name + '_R1.fastq'
	R2 = name + '_R2.fastq'
	orig = os.getcwd()
	print(orig + '/' + TO_BE_PROCESSED + '/' + R1)
	print(DATA_DIRECTORY + '/input_R1.fastq')
	os.rename(orig + '/' + TO_BE_PROCESSED + '/' + R1, DATA_DIRECTORY + '/input_R1.fastq')
	os.rename(orig + '/' + TO_BE_PROCESSED + '/' + R2, DATA_DIRECTORY + '/input_R2.fastq')
	# do something with the log text file!

def deletefiles():
	for name in os.listdir('/home/cc/DataProcessing'):
		os.remove('/home/cc/DataProcessing/' + name)
	for name in os.listdir('/home/cc/Uploads'):
                os.remove('/home/cc/Uploads/' + name)
	return True

#def prepenv():
	# this function should create directories in the instance to ensure that everything is correct
	# should be done after downloading files
	

def prepref(logfile):
        # prepare reference genome for use by calling prepareref.json
        if runp.runjsoncommands(JSON_DIRECTORY + 'prepareref.json', logfile):
                print('Preparing Reference Genome was successful.')

def checkref(logfile):
        # first check for hg19 database:
        if not os.listdir(HG19_DIRECTORY):
                chdir(DOWNLOAD_DIRECTORY)
                print('HG19 database is not present. Need to download.')
                osf.downloadfiles(CONTAINER, HG19_FOLDER, False)
		if moveref('data'): # does this work?
                        print('Reference moved correctly.')
        else:
                print('HG19 database is already present in server!')
        if not os.listdir(REF_DIRECTORY):
                chdir(DOWNLOAD_DIRECTORY)
                print('Reference Genome is not present. Need to download.')
                osf.downloadfiles(CONTAINER, REF_FOLDER, False)
		if moveref('genome'): # does this work?
			print('Reference moved correctly.')
        elif len(os.listdir(REF_DIRECTORY)) is 1:
                chdir(REF_DIRECTORY)
                print('Reference Genome is downloaded but needs to be prepared -- beginning process.')
                prepref(logfile)
        else:
                print('Reference Genome is already present in server and prepared!')
        return True

def moveref(name):
	# move downloaded files from downloads file to reference folders
	# currently hardcoding names
	if name is 'genome':
		os.rename(DOWNLOAD_DIRECTORY + '/ReferenceData/genome_sorted.fa', REF_DIRECTORY + 'genome_sorted.fa')
	elif name is 'data':
		os.rename(DOWNLOAD_DIRECTORY + '/HG19Data/dbsnp_135.hg19.sort.vcf', HG19_DIRECTORY + '/dbsnp_135.hg19.sort.vcf')
	else:
		print('Input string neither genome nor data! Error!')
	return True
