import logging

from swiftclient.service import SwiftService, SwiftError
from sys import argv

logging.basicConfig(level=logging.ERROR)
logging.getLogger("requests").setLevel(logging.CRITICAL)
logging.getLogger("swiftclient").setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)

def is_filetype(x):
    return (
        x["name"].lower().endswith(argv[2])
    )

container = argv[1]
with SwiftService() as swift:
    	try:
        	list_parts_gen = swift.list(container=container)
        	for page in list_parts_gen:
            		if page["success"]:
                		for item in page["listing"]:
					if is_filetype(item):	
						i_size = int(item["bytes"])
                      				i_name = item["name"]
                        			i_etag = item["hash"]
                        			print("%s [size: %s] [etag: %s]" %(i_name, i_size, i_etag))
            		else:
                		raise page["error"]

    	except SwiftError as e:
        	logger.error(e.value)
