#!/usr/bin/env python
from swiftclient.service import SwiftService, SwiftError, SwiftUploadObject
from novaclient.client import Client
import os

# this file contains all of the created openstack functions
# --> used to call functions in other scripts


# credential functions
def getkeystonecreds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['tenant_name'] = os.environ['OS_TENANT_NAME']
    return d
 
def getnovacreds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    return d

def getnovacreds_v2():
    d = {}
    d['version'] = '2'
    d['username'] = os.environ['OS_USERNAME']
    d['api_key'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['project_id'] = os.environ['OS_TENANT_NAME']
    return d

# swift functions:
# define function to check for certain file type
def isfiletype(x, filetype):
    	return (
        	x["name"].lower().endswith(filetype)
    	)

# check if file is present in folder or not
def filepresent(container, folder, filetype):
	# first argument is container name 
  	# second argument is folder name
	list_options = {"prefix": folder}
	with SwiftService() as swift:
    		try:
        		list_parts_gen = swift.list(container=container, options=list_options)
        		for page in list_parts_gen:
            			if page["success"]:
                			for item in page["listing"]:
						if isfiletype(item, filetype):
							return True
					return False
            			else:
                			raise page["error"]

    		except SwiftError as e:
			print('Error: %s' %e)

# print out the contents of an folder --> given filetype
def listcontents(container, folder, filetype):
	list_options = {"prefix": folder}
	with SwiftService() as swift:
		try:
			list_parts_gen = swift.list(container=container, options=list_options)
			for page in list_parts_gen:
				if page["success"]:
					for item in page["listing"]:
						if isfiletype(item, filetype):
							size = int(item["bytes"])
							name = item["name"]
							etag = item["hash"]
							print("%s [size: %s] [etag: %s]" %(name, size, etag))
				else:
					raise page["error"]
		except SwiftError as e:
			print("SwiftError: %s" %e)

# delete a list of objects in a container
def deletefiles(container, objs):
	# first argument is the container where objects are located
	# second argument is a list containing all of the objects to delete
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

# download and then optionally delete files in a container
def downloadfiles(container, folder, delete_flag):
	# argument one is the container name
	# argument two is the folder name within the container
	# argument three is a flag to delete file from container if set true
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

# upload a list of objects to a container
def uploadfiles(container, options, objs):
# first argument is the container to upload file to
# second argument is a dictionary of the options to supply to SwiftUploadObject 
# third argument is a list of the files to upload
	with SwiftService() as swift:
    		try:
			# create the SwiftUploadObject list of objects to upload
			#objs = [SwiftUploadObject(obj, options=options) for obj in objs]
			objs = [SwiftUploadObject(obj) for obj in objs]
        		# Schedule uploads on the SwiftService thread pool and iterate over the results
        		#for result in swift.upload(container, objs):
			for result in swift.upload(container, objs):
            			if result['success']:
                			if 'object' in result:
                    				print("Successfully uploaded %s." %result['object'])
                			elif 'for_object' in result:
                    				print('%s segment %s' % (result['for_object'],result['segment_index']))
            			else:
                			error = result['error']
                			if result['action'] == "create_container":
                    				print('Warning: failed to create container '"'%s'%s", container, error)
                			elif result['action'] == "upload_object":
                    				print("Failed to upload object %s to container %s: %s" %(container, result['object'], error))
                			else:
                    				print("%s" % error)
    		except SwiftError as e:
			print("SwiftError: %s" %e)

# nova functions:
# delete server given the server name
def deleteserver(name):
	  # grab the nova credentials from credentials.py
	  creds = get_nova_creds_v2()
	  nova = Client(**creds)
 
	  servers_list = nova.servers.list()
	  server_exists = False

	  for s in servers_list:
		  if s.name == name:
			  server_exists = True
			  break
	  if not server_exists:
		  print("The server %s does not exist." % name)
	  else:
		  print("Deleting server: %s" % name)
		  server = nova.servers.find(name=name)
		  server.delete()
		  print("The server %s was deleted." % name)

# associate floating ip address to a server
def associateip(name):
	  # get nova credentials
	  credentials = get_nova_creds_v2()
	  nova_client = Client(**credentials)

	  # create a new floating ip from the addresses available
	  ip_list = nova_client.floating_ip_pools.list()
	  floating_ip = nova_client.floating_ips.create(ip_list[0].name)

  	# assign the created ip address to the instance input by user
	  instance = nova_client.servers.find(name)
	  instance.add_floating_ip(floating_ip)
