import time

from twisted.words import service
from ircuser import IRCUser
from twisted.internet.protocol import Factory

class IRCUserFactory(Factory):
    protocol = IRCUser

    def __init__(self, slackProtocol):
        self.connections = []
        self.slackProtocol = slackProtocol
        self.creationTime = time.ctime()

    def sendMessage(self, sender, recipient, text):
        for connection in self.connections:
            connection.sendCommand("PRIVMSG", (recipient, text), sender)
