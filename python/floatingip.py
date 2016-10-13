#!/usr/bin/env python

from credentials import get_nova_creds_v2
from novaclient.client import Client

credentials = get_nova_creds_v2()
nova_client = Client(**credentials)
ip_list = nova_client.floating_ips.list()
for item in ip_list:
	print(item)
