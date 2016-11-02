This folder contains scripts to perform certain tasks using the Openstack Python APIs:
  
  -python-keystoneclient : Identity Service : 
	http://docs.openstack.org/developer/python-keystoneclient/
  -python-glanceclient : Image Service : 
	http://docs.openstack.org/developer/python-glanceclient/
  -python-novaclient : Compute Service : 
	http://docs.openstack.org/developer/python-novaclient/
  -python-quantumclient : Networking Service : 
	http://docs.openstack.org/developer/python-quantumclient/
  -python-cinderclient : Block Storage Service : 
	http://docs.openstack.org/developer/python-cinderclient/
  -python-swiftclient : Object Storage Service : 
	http://docs.openstack.org/developer/python-swiftclient/

To follow: instructions on how to use the scripts in this folder for your own project.

openstackfunctions.py contains the following functions (showing function name and how to call in a different script):

from openstackfunctions import *

1. filepresent

filepresent("container name", "folder name", "filetype")

2. Three credential functions:
  1. "getkeystonecreds"
  2. "getnovacreds"
  3. "getnovacredsv2"

novacreds = getnovacreds()
nova = Client(\*\*creds)
nova2creds = getnovacredsv2()
nova = Client(\*\*creds)

3. deleteserver

deleteserver("server name")

4. downloadfiles

downloadfiles("container name", "folder name")

5. listcontents

listcontents("container name", "folder name", "filetype")

6. associateip

associateip("servername")

7. uploadfiles:

objectlist = ["filename1", "filename2", "filename3"]
uploadfiles("container name", [objectlist])
