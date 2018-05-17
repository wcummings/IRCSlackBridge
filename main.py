import sys

from twisted.internet import reactor
from twisted.python import log
from twisted.words import service
from slackrealtime import connect
from slackrealtime.factory import DyingWebSocketClientFactory
from slackprotocol import SlackProtocol

SLACK_API_TOKEN = os.getenv("SLACK_API_TOKEN")

if __name__ == '__main__':
    log.startLogging(sys.stdout)

    connection = connect(SLACK_API_TOKEN,
                         protocol=lambda *a,**k: SlackProtocol(*a,**k).init(),
                         factory=DyingWebSocketClientFactory)
    
    reactor.run()
