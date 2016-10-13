# this script checks the Swift Container for files being uploaded to be processed
# note: script needs to log into Chameleon to access the swift container
# author: Andrew K Boles
import os, re, time, sys
from selenium import webdriver

def checkSwiftContainer(username, password, project, container):
	#provide credentials to log into Chameleon Project
	browser = webdriver.PhantomJS(executable_path='/usr/local/lib/phantom/bin/phantomjs')
	browser.get('https://chi.tacc.chameleoncloud.org/dashboard/auth/login/')
	usernameText = browser.find_element_by_id('id_username')
	usernameText.send_keys(username)
	passwordText = browser.find_element_by_id('id_password')
	passwordText.send_keys(password)
	passwordText.submit()
	projectName = 'https://chi.tacc.chameleoncloud.org/dashboard/auth/switch/' + project
	browser.get(projectName)
    	# continually check the desired Swift Container for new files to be processed
	print('Logged onto Chameleon Project, now going to check for files to process.')
	containerName = 'https://chi.tacc.chameleoncloud.org/dashboard/project/containers/' + container + '/to_be_processed/'
	browser.get(containerName)
	while 'No items to display.' in browser.find_element_by_id('objects').text:
    		print('Still no items to be processed.')
    		time.sleep(10)
    		browser.get(containerName)
	filenames = []
        for item in browser.find_element_by_id('objects').text.encode('ascii', 'ignore').split():
                if '.fastq' in item:
                        filenames.append(item)
        with open('filename.txt', 'w') as f:
                f.write('\n'.join(filenames))
        browser.close()
        browser.quit()
        return

# now to call function and make sure it can restart itself if it reaches an exception
# need to get log-in credentials from somewhere other than this file
#sys.stdout = open('log', 'a')
userCred = []
with open('loginCredentials.txt', 'r') as f:
	for line in f:
		userCred.append(line.rstrip())
while True:
	try:
		checkSwiftContainer(userCred[0], userCred[1], userCred[2], userCred[3])
	except Exception:
		print('User was logged off. Starting checkSwiftContainer function again.')
		pass
	else:
		print('Done checking Swift Container. Starting to run the pipeline commands.')
		break

# now open runPipeline.py
os.system('python runPipeline.py')
