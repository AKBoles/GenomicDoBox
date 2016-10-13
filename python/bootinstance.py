import os
import time
import novaclient.v1_1.client as nvclient
from credentials import get_nova_creds
creds = get_nova_creds()
nova = nvclient.Client(**creds)
image = nova.images.find(name="CC-Ubuntu14.04")
flavor = nova.flavors.find(name="baremetal")
instance = nova.servers.create(name="test", image=image, flavor=flavor, key_name="akb-public-key", reservation_id="9e818da1-cd71-4853-833a-436c6f6340a7")
 
# Poll at 5 second intervals, until the status is no longer 'BUILD'
status = instance.status
while status == 'BUILD':
    time.sleep(5)
    # Retrieve the instance again so the status field updates
    instance = nova.servers.get(instance.id)
    status = instance.status
print "status: %s" % status
