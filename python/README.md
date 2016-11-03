Python Code
=============

### Folder Contents ###

The following is an updated list of the python folder contents. The script is marked as "working", "in-progress, working", or "in-progress, not working".

1. bootinstance.py : in-progress, not working

> This script will be used to boot a new bare metal instance in Chameleon Cloud.
> Currently receiving an error when the instance is built dealing with host allocation.

2. openstackfunctions.py : working

> 1. filepresent("container name", "folder name", "filetype")
>
> 2. Three credential functions:
>
>      *novacreds = getnovacreds()
>    
>   *nova = Client(\*\*creds)
>    
>   *nova2creds = getnovacredsv2()
>    
>   *nova = Client(\*\*creds)
>
> 3. deleteserver("server name")
>
> 4. downloadfiles("container name", "folder name")
>
> 5. listcontents("container name", "folder name", "filetype")
>
> 6. associateip("servername")
>
> 7. uploadfiles("container name", [objectlist])
>

3. orchestration.py : in-progress, working

> information about this

4. runpipeline.py - working

> information about this

### OpenStack Links ###

1. python-keystoneclient : Identity Service : http://docs.openstack.org/developer/python-keystoneclient/

2. python-glanceclient : Image Service : http://docs.openstack.org/developer/python-glanceclient/

3. python-novaclient : Compute Service : http://docs.openstack.org/developer/python-novaclient/

4. python-quantumclient : Networking Service : http://docs.openstack.org/developer/python-quantumclient/
	
5. python-cinderclient : Block Storage Service : http://docs.openstack.org/developer/python-cinderclient/
	
6. python-swiftclient : Object Storage Service : http://docs.openstack.org/developer/python-swiftclient/
