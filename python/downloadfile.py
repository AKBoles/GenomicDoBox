#!/usr/bin/env python
from swiftclient.service import SwiftService, SwiftError

def download_files(container, folder):
	# argument one is the container name
	with SwiftService() as swift:
    		try:
			# argument two is the folder name within the container
        		list_options = {"prefix": folder}
        		list_parts_gen = swift.list(container=container, options=list_options)
        		for page in list_parts_gen:
            			if page["success"]:
                			objects = [obj["name"] for obj in page["listing"]]
					for result in swift.download(container=container, objects=objects):
						if result["success"]:
							print("Downloaded %s successfully." %result["object"])
						else:
							print("Failed to download %s." %result["object"])
            			else:
                			raise page["error"]
    		except SwiftError as e:
			print('Error: %s' %e)
