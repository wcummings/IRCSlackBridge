import sys

from twisted.cred import checkers, portal
from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.python import log
from twisted.words import service
from slackrealtime import connect
from slackrealtime.factory import DyingWebSocketClientFactory
from slackprotocol import SlackProtocol
from ircuser import IRCUser
from ircuserfactory import IRCUserFactory

SLACK_API_TOKEN = os.getenv("SLACK_API_TOKEN")

if __name__ == '__main__':
    log.startLogging(sys.stdout)

    ircfactory = IRCUserFactory()
    rtm_connection = connect(SLACK_API_TOKEN,
                             protocol=lambda *a,**k: SlackProtocol(*a,**k).init(ircfactory),
                             factory=DyingWebSocketClientFactory)

    endpoint = TCP4ServerEndpoint(reactor, 6667)
    endpoint.listen(ircfactory)
    
    reactor.run()
