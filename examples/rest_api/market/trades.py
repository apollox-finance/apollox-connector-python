import logging
from apollox.rest_api import Client
from apollox.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

client = Client()
logging.info(client.trades("BTCUSDT", limit=500))
