import novaclient.v1_1.client as nvclient
from credentials import get_nova_creds
import sys

# retrieve server name from command line input
name = sys.argv[1]

# grab the nova credentials from credentials.py
creds = get_nova_creds()
nova = nvclient.Client(**creds)
 
server = nova.servers.find(name=name)
server.delete()

print(nova.servers.list())
