# -*- coding: utf-8 -*-

from nose.tools import raises

from module.remote.ttypes import Forbidden
from module.remote.JSONClient import JSONClient

class TestJSONBackend:

    def setUp(self):
        self.client = JSONClient()

    def test_login(self):
        self.client.login("User", "test")
        self.client.getServerVersion()
        self.client.logout()

    def test_wronglogin(self):
        ret = self.client.login("WrongUser", "wrongpw")
        assert ret == False

    @raises(Forbidden)
    def test_access(self):
        self.client.getServerVersion()

    @raises(AttributeError)
    def test_unknown_method(self):
        self.client.login("User", "test")
        self.client.sdfdsg()

    # TODO: test raising of exceptions, also in WSBackend