# -*- coding: utf-8 *-*
import pexpect


class Console(object):

    TIMEOUT = 0.2

    def __init__(self, prog, timeout=TIMEOUT):
        self.process = pexpect.spawn(prog)
        self._timeout = timeout

    def read(self):
        response = ''
        while True:
            try:
                self.process.expect('\r\n', self._timeout)
                response += '\n' + self.process.before
            except pexpect.TIMEOUT:
                break
            except pexpect.EOF:
                break
        return response

    def cmd(self, command):
        self.process.sendline(command)
        return self.read()
