# -*- coding: utf-8 *-*
import pexpect


class Console(object):

    TIMEOUT = 0.2

    def __init__(self, prog, timeout=TIMEOUT):
        self._process = pexpect.spawn(prog)
        self._timeout = timeout

    def read(self):
        response = ''
        while True:
            try:
                self._process.expect('\r\n', self._timeout)
                response += '\n' + self._process.before
            except pexpect.TIMEOUT:
                break
            except pexpect.EOF:
                break
        return response

    def cmd(self, command):
        self._process.sendline(command)
        return self.read()
