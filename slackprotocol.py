from slackrealtime import RtmProtocol
from slackrealtime.event import Message
import json

class SlackProtocol(RtmProtocol):

    def init(self, ircfactory):
        self.ircfactory = ircfactory
        return self

    def onOpen(self):
        self.factory.connection = self
        print "Connected to Slack"

    def onSlackEvent(self, event):
        if not isinstance(event, Message):
            return

        # if not hasattr(event, 'user') or event.user == 'USLACKBOT' or event.user == self.meta.me['id']:
        #     return

        user = self.meta.users.get(event.user, None)
        channel = self.meta.channels.get(event.channel, None)

        print "SLACK MESSAGE: (#%s) %s: %s" % (channel['name'], user['name'], event.text)

        self.ircfactory.sendMessage(user['name'], "#%s" % channel['name'], event.text)
