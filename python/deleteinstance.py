from novaclient.client import Client
from credentials import get_nova_creds_v2
import sys

# retrieve server name from command line input
name = sys.argv[1]

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
