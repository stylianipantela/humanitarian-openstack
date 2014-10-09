from libcloud.storage.types import Provider
from libcloud.storage.providers import get_driver


class StorageServer(Server):
    def __init__(self, config):
      # Connect to Rackspace Cloud Files in the IAD datacenter.
      Driver = get_driver(Provider.CLOUDFILES)
      storage = Driver(config["identity"], ["identity"], region="iad")
