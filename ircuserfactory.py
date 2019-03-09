import time

from twisted.words import service
from ircuser import IRCUser
from twisted.internet.protocol import Factory

class IRCUserFactory(Factory):
    protocol = IRCUser

    def __init__(self, slack_api_token):
        self._slack_api_token = slack_api_token

    def buildProtocol(self, addr):
        return IRCUser(self._slack_api_token)
