import os, sys, re, json, time
import collections

def runjsoncommands(filename):
	# Open the config file containing the commands, load into ordered dictionary
	command_file = open(filename)
	commands = json.load(command_file, object_pairs_hook=collections.OrderedDict)
	command_file.close()
	#Traverse through cmd config file structure
	stepNum = 1
	for step in commands:
		print('Beginning Step: %s' %stepNum)
		for cmdNum in commands[step]:
			cmd = commands[step][cmdNum]
			os.popen(cmd)
			time.sleep(1)
			out = os.popen(cmd).read()
		stepNum = stepNum + 1
	return
