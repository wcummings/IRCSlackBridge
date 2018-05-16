from twisted.words.protocols import irc

class IRCUser(irc.IRC):

    def connectionMade(self):
        irc.IRC.connectionMade(self)
        self.factory.connections.append(self)

    def connectionLost(self, reason):
        irc.IRC.connectionLost(self, reason)        
        self.factory.connections.remove(self)
        
    def irc_unknown(self, prefix, command, params):
        print "Unknown command: %s" % command
        self.sendCommand(irc.ERR_UNKNOWNCOMMAND, (command, ":Unknown command"))

    def irc_NICK(self, prefix, params):
        self.sendMessage(irc.RPL_WELCOME, params[0], ":Welcome to the Internet Relay Network %s" % params[0])

    def irc_PRIVMSG(self, prefix, params):
        channel = params[0].replace("#", "")
        text = params[1]

    # TODO
    def irc_JOIN(self, prefix, params):
        self.sendMessage(irc.RPL_TOPIC, ":")
    
    def irc_PING(self, prefix, params):
        self.sendLine("PONG %s" % params[-1])        
