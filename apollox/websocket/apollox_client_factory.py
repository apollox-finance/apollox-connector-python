import logging
from autobahn.twisted.websocket import WebSocketClientFactory
from twisted.internet.protocol import ReconnectingClientFactory
from apollox.websocket.apollox_client_protocol import ApolloxClientProtocol


class ApolloxReconnectingClientFactory(ReconnectingClientFactory):

    initialDelay = 0.1
    maxDelay = 10
    maxRetries = 10


class ApolloxClientFactory(WebSocketClientFactory, ApolloxReconnectingClientFactory):
    def __init__(self, *args, payload=None, **kwargs):
        WebSocketClientFactory.__init__(self, *args, **kwargs)
        self.protocol_instance = None
        self.base_client = None
        self.payload = payload

    _reconnect_error_payload = {"e": "error", "m": "Max reconnect retries reached"}

    def startedConnecting(self, connector):
        logging.info("Start to connect....")

    def clientConnectionFailed(self, connector, reason):
        logging.error(
            "Can't connect to server. Reason: {}. Retrying: {}".format(
                reason, self.retries + 1
            )
        )
        self.retry(connector)
        if self.retries > self.maxRetries:
            self.callback(self._reconnect_error_payload)

    def clientConnectionLost(self, connector, reason):
        logging.error(
            "Lost connection to Server. Reason: {}. Retrying: {}".format(
                reason, self.retries + 1
            )
        )
        self.retry(connector)
        if self.retries > self.maxRetries:
            self.callback(self._reconnect_error_payload)

    def buildProtocol(self, addr):
        return ApolloxClientProtocol(self, payload=self.payload)
