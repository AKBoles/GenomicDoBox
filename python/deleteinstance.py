from novaclient.client import Client
from credentials import get_nova_creds_v2
import sys

# retrieve server name from command line input
name = sys.argv[1]

# grab the nova credentials from credentials.py
creds = get_nova_creds_v2()
nova = Client(**creds)
 
server = nova.servers.find(name=name)
server.delete()

print(nova.servers.list())
