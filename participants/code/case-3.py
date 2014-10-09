# CASE 2: 2 WEB SERVERS, 2 DATABASE SERVER2, 1 LOAD BALANCER FOR DBS AND ONE FOR SERVER 
# WITH HA PROXY
from config import get_config
from oslogger import log
from db_node import DBServer
from ha_node import HAProxyServer
from web_node import WebServer

# storage
from libcloud.storage.types import Provider
from libcloud.storage.providers import get_driver
from io import BytesIO

import libcloud.security
libcloud.security.VERIFY_SSL_CERT = False

if __name__ == "__main__":
    config = get_config()

    log.info("Creating web node.")
    web_server = WebServer(config)
    server_node = web_server.create_node("server-stella")

    log.info("Creating database node.")
    db_server = DBServer(config)
    db_node = db_server.create_node("db-stella")

    # drives and storing files

    Driver = get_driver(Provider.CLOUDFILES)
    storage = Driver(config["identity"], config["credential"], config["region"])
    container = storage.create_container("my_container_stella")
    obj = container.upload_object_via_stream(BytesIO("some_data"),
                                         object_name="my_uploaded_data_stella")
    stream = obj.as_stream()
    data = next(stream)
    print "Did we succeed?"
    print data

