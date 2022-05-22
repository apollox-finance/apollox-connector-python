import logging
from apollox.rest_api import Client
from apollox.lib.utils import config_logging
from apollox.error import ClientError

config_logging(logging, logging.DEBUG)

key = ""
secret = ""

client = Client(key, secret, base_url="https://fapi.apollox.finance")

try:
    response = client.countdown_cancel_order(symbol = "BTCUSDT",countdownTime=1000, recvWindow=2000)
    logging.info(response)
except ClientError as error:
    logging.error(
        "Found error. status: {}, error code: {}, error message: {}".format(
            error.status_code, error.error_code, error.error_message
        )
    )