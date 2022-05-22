import logging
from apollox.rest_api import Client
from apollox.lib.utils import config_logging
from apollox.error import ClientError

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

client = Client(key, secret, base_url="https://fapi.apollox.finance")

try:
    response = client.new_order(symbol="BTCUSDT", side = "SELL", type= "LIMIT", quantity= 0.001, timeInForce="GTC", price= 59808.02)
    logging.info(response)
except ClientError as error:
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )
