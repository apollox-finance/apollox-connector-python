import logging
from apollox.rest_api import Client
from apollox.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

client = Client()
logging.info(client.index_price_klines("BTCUSDT", "1d", **{"limit": 500}))