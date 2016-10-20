This folder contains scripts to perform certain tasks using the Openstack Python APIs:
  
  -python-keystoneclient : Identity Service : http://docs.openstack.org/developer/python-keystoneclient/
  -python-glanceclient : Image Service : http://docs.openstack.org/developer/python-glanceclient/
  -python-novaclient : Compute Service : http://docs.openstack.org/developer/python-novaclient/
  -python-quantumclient : Networking Service : http://docs.openstack.org/developer/python-quantumclient/
  -python-cinderclient : Block Storage Service : http://docs.openstack.org/developer/python-cinderclient/
  -python-swiftclient : Object Storage Service : http://docs.openstack.org/developer/python-swiftclient/

To follow: instructions on how to use the scripts in this folder for your own project.

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

3. deleteinstance.py:   
To use in another python script:

