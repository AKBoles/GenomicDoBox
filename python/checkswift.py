#!/usr/bin/env python
from swiftclient.service import SwiftService, SwiftError
from sys import argv

# define function to check for certain file type
def is_filetype(x, filetype):
    	return (
        	x["name"].lower().endswith(filetype)
    	)

# first argument is container name 
# second argument is folder name
# third argument is the filetype
container = argv[1]
folder = argv[2]
filetype = argv[3]
list_options = {"prefix": folder}
with SwiftService() as swift:
  	try:
        	list_parts_gen = swift.list(container=container, options=list_options)
        	for page in list_parts_gen:
            		if page["success"]:
                		for item in page["listing"]:
					if is_filetype(item, filetype):	
						return True
				return False
            		else:
                		raise page["error"]
    	except SwiftError as e:
		print('Error: %s' %e)
