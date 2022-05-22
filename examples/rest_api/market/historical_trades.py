import logging
from apollox.rest_api import Client
from apollox.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ""

# historical_trades requires api key in request header
client = Client(key = key)
logging.info(client.historical_trades("BTCUSDT", **{"limit" : 10}))