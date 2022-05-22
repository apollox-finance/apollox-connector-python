#!/usr/bin/env python
import logging
from apollox.rest_api import Client
from apollox.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

key = ""

client = Client(key, base_url="https://fapi.apollox.finance")
logging.info(client.renew_listen_key(""))
