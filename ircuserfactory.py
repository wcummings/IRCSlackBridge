from twisted.words import service
from ircuser import IRCUser
from twisted.internet.protocol import Factory

class IRCUserFactory(Factory):
    protocol = IRCUser

    def __init__(self):
        self.connections = []

    def sendMessage(self, sender, recipient, text):
        for connection in self.connections:
            connection.sendCommand("PRIVMSG", (recipient, text), sender)
