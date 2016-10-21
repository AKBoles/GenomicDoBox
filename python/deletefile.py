#!/usr/bin/env python
from swiftclient.service import SwiftService, SwiftError
from sys import argv

# first argument is the container where objects are located
# second argument is a list containing all of the objects to delete
container = argv[1]
objs = []
for item in argv[2:]:
	objs.append(item)
with SwiftService() as swift:
    	try:
		delete_iter = swift.delete(container=container, objects=objs)
       		for result in delete_iter:
         		if result["success"]:
				print('Object %s was successfully deleted.' %result.get('object',''))
            		else:
				print('Object %s was not successfully deleted.' %result.get('object',''))
    	except SwiftError as e:
		print('Error: %s' %e)
