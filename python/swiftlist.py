#!/usr/bin/env python
from swiftclient.service import SwiftService, SwiftError
from sys import argv

def is_filetype(x, filetype):
	return(x["name"].lower().endswith(filetype))

def list_contents(container, folder, filetype):
# first argument is container name
# second argument is folder name
# third argument is filetype
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
						size = int(item["bytes"])
						name = item["name"]
						etag = item["hash"]
						print("%s [size: %s] [etag: %s]" %(name, size, etag))
			else:
				raise page["error"]
	except SwiftError as e:
		print("SwiftError: %s" %e)
