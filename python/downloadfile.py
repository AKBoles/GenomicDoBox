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
                			objects = [
                    				obj["name"] for obj in page["listing"]
                			]
                			for down_res in swift.download(container=container,objects=objects):
                    				if down_res['success']:
                        				print("'%s' downloaded" % down_res['object'])
                    				else:
                        				print("'%s' download failed" % down_res['object'])
						print('stuck here?')
            			else:
                			raise page["error"]
    		except SwiftError as e:
			print('Error: %s' %e)
	return
