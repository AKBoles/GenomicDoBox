#!/usr/bin/env python
from swiftclient.service import SwiftService, SwiftError
from sys import argv

# argument one is the container name
# argument two is the folder name within the container
# argument three is a flag to delete file from container if set true
container = argv[1]
folder = argv[2]
delete_flag = bool(argv[3])
with SwiftService() as swift:
    	try:
       		list_options = {"prefix": folder}
       		list_parts_gen = swift.list(container=container, options=list_options)
       		for page in list_parts_gen:
           		if page["success"]:
               			objects = [obj["name"] for obj in page["listing"]]
				for result in swift.download(container=container, objects=objects):
					if result["success"]:
						print("Downloaded %s successfully." %result["object"])
						if delete_flag:
							delete_files(container, objects)				
					else:
						print("Failed to download %s." %result["object"])
            		else:
               			raise page["error"]
    	except SwiftError as e:
		print('Error: %s' %e)
