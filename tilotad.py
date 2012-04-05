#!/usr/bin/python
# -*- coding: utf-8 *-*
import daemon
from console import Console
import zmq
import settings


class Daemon(object):

    def __init__(self, fake=False):
        self._fake = fake

    def initialize(self):
        pass

    def run(self):
        pass

    def start(self):
        if self._fake:
            self.initialize()
            self.run()
        else:
            with daemon.DaemonContext():
                self.initialize()
                self.run()


class TilotaDaemon(Daemon):

    def initialize(self):
        self._coordinator = Console('dmtcp_coordinator')
        self._coordinator.read()
        self._inbox = zmq.Socket(zmq.Context(), zmq.PULL)
        self._inbox.bind(settings.DAEMON_INBOX)
        self.CALLBACKS = {
            'get_game_id': self.get_game_id
        }

    def _dispatch(self, message):
        message_name = message.get('name', None)
        if message_name in self.CALLBACKS:
            self.CALLBACKS[message_name](message)

    def get_game_id(self, message):
        print self._coordinator.cmd('l')

    def run(self):
        while True:
            message = self._inbox.recv_json()
            self._dispatch(message)


if __name__ == '__main__':
    TilotaDaemon(fake=True).start()
