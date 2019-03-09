import sys
import os

from twisted.internet import reactor
from twisted.python import log
from twisted.words import service
from twisted.internet.endpoints import TCP4ServerEndpoint

from ircuserfactory import IRCUserFactory

SLACK_API_TOKEN = os.getenv("SLACK_API_TOKEN")


if __name__ == '__main__':
    log.startLogging(sys.stdout)
    endpoint = TCP4ServerEndpoint(reactor, 6667)
    endpoint.listen(IRCUserFactory(SLACK_API_TOKEN))
    reactor.run()
