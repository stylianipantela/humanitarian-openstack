# CASE 2: 2 WEB SERVERS, 2 DATABASE SERVER2, 1 LOAD BALANCER FOR DBS AND ONE FOR SERVER 
# WITH HA PROXY
from config import get_config
from oslogger import log
from db_node import DBServer
from ha_node import HAProxyServer
from web_node import WebServer

import libcloud.security
libcloud.security.VERIFY_SSL_CERT = False

if __name__ == "__main__":
    config = get_config()

    log.info("Creating web nodes.")
    server_nodes = []
    web_server = WebServer(config)
    for name in ("server-1-stella", "server-2-stella"):
        server_nodes.append(web_server.create_node(name))

    log.info("Creating database nodes.")
    db_nodes = []
    db_server = DBServer(config)
    for name in ("db-1-stella", "db-2-stella"):
      db_nodes.append(db_server.create_node(name))

    log.info("Creating haproxy load balancer node for servers.")
    haproxy_server = HAProxyServer(config, server_nodes)

    log.info("Creating haproxy load balancer node for dbs.")
    haproxy_db = HAProxyServer(config, db_nodes)

    lb_node_server = haproxy_server.create_node("haproxy-stella-servers")
    lb_node_db = haproxy_db.create_node("haproxy-stella-dbs")

    log.info("Access the load balancer at %s for db", lb_node_server.public_ips)
    log.info("Access the load balancer at %s for server", lb_node_db.public_ips)

