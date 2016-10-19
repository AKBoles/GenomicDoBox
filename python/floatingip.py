#!/usr/bin/env python

from credentials import get_nova_creds_v2
from novaclient.client import Client

# get nova credentials
credentials = get_nova_creds_v2()
nova_client = Client(**credentials)

# create a new floating ip from the addresses available
ip_list = nova_client.floating_ip_pools.list()
floating_ip = nova_client.floating_ips.create(ip_list[0].name)

# assign the created ip address to the instance input by user
instance = nova_client.servers.find(name=sys.argv[1])
instance.add_floating_ip(floating_ip)
