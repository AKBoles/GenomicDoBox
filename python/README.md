This folder contains scripts to perform certain tasks using the Openstack Python APIs:
  
  -python-keystoneclient : Identity Service : http://docs.openstack.org/developer/python-keystoneclient/
  -python-glanceclient : Image Service : http://docs.openstack.org/developer/python-glanceclient/
  -python-novaclient : Compute Service : http://docs.openstack.org/developer/python-novaclient/
  -python-quantumclient : Networking Service : http://docs.openstack.org/developer/python-quantumclient/
  -python-cinderclient : Block Storage Service : http://docs.openstack.org/developer/python-cinderclient/
  -python-swiftclient : Object Storage Service : http://docs.openstack.org/developer/python-swiftclient/

To follow: instructions on how to use the scripts in this folder for your own project.
Note: Will move all of these to one python script after they are all written.

1. checkswift.py: contains function "file_present". This checks whether a certain container contains a specific filetype.  
To use in another python script:

from checkswift import file_present

file_present("container_name", "folder_name", "filetype")

2. credentials.py: contains three functions:
  1. "get_keystone_creds"
  2. "get_nova_creds"
  3. get_nova creds_v2"
To use in another python script:

from novaclient.client import Client
from credentials import *

novacreds = get_nova_creds()
nova = Client(\*\*creds)
nova2creds = get_nova_creds_v2()
nova = Client(\*\*creds)

3. deleteinstance.py: contains function "delete_server". This deletes a server whose name is input.
To use in another python script:

from deleteinstance import delete_server

delete_server("server_name")

4. downloadfile.py: contains function "download_files". This downloads all files from a specific folder in a container.
To use in another python script:

from downloadfile import download_files

download_files("container_name", "folder_name")

5. swiftlist.py: contains function "list_contents". This lists all of the files.fileype present in a specific folder in a container.
To use in another python script:

from swiftlist import list_contents

list_contents("container_name", "folder_name", "filetype")

6. floatingip.py: contains function "associate_ip". This assigns an ip address to an input server.
To use in another python script:

from floatingip import associate_ip

associate_ip("server_name")

7. uploadfile.py: contains function "upload_files". This uploads an input list of objects to a specified container.
To use in another python script:

from uploadfile import upload_files

object_list = ["filename1", "filename2", "filename3"]
upload_files("container_name", object_list)
