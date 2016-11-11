import os, sys, re, json, time
import collections

def chdir(dest):
        old = os.getcwd()
        os.chdir(dest)
        new = os.getcwd()
        print('old: %s, new: %s' %(old, new))

def setupenv():
	# write the function that will setup the environment needed after downloading files

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
