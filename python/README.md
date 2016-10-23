This folder contains scripts to perform certain tasks using the Openstack Python APIs:
  
  `-python-keystoneclient` : Identity Service : http://docs.openstack.org/developer/python-keystoneclient/    
  `-python-glanceclient` : Image Service : http://docs.openstack.org/developer/python-glanceclient/    
  `-python-novaclient` : Compute Service : http://docs.openstack.org/developer/python-novaclient/    
  `-python-quantumclient` : Networking Service : http://docs.openstack.org/developer/python-quantumclient/    
  `-python-cinderclient` : Block Storage Service : http://docs.openstack.org/developer/python-cinderclient/    
  `-python-swiftclient` : Object Storage Service : http://docs.openstack.org/developer/python-swiftclient/    

To follow: instructions on how to use the scripts in this folder for your own project.    

`openstackfunctions.py` contains the following functions (showing function name and how to call in a different script):    

`from openstackfunctions import *`    

1. file_present    
    ```
    file_present("container_name", "folder_name", "filetype")
    ```    
    
2. Three credential functions:    

    1. "get_keystone_creds"
    2. "get_nova_creds"
    3. get_nova creds_v2"
    ```
    novacreds = get_nova_creds()    
    nova = Client(\*\*creds)    
    nova2creds = get_nova_creds_v2()    
    nova = Client(\*\*creds)    
    ```    
    
3. delete_server    
    ```
    delete_server("server_name")
    ```    
    
4. download_files    
    ```
    download_files("container_name", "folder_name")
    ```    
    
5. list_contents    
    ```
    list_contents("container_name", "folder_name", "filetype")
    ```    
    
6. associate_ip    
    ```
    associate_ip("server_name")
    ```    
    
7. upload_files:    
    ```
    object_list = ["filename1", "filename2", "filename3"]
    upload_files("container_name", object_list)
    ```
