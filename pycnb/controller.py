#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
log = logging.getLogger(__name__)

import re
from cement.core import foundation, controller, handler
from pprint import pprint

from twisted.internet import reactor
from twisted.web.client import Agent
from twisted.web.http_headers import Headers
from twisted.internet.defer import Deferred
from twisted.internet.protocol import Protocol

class DailyRatesProtocol(Protocol):
    def __init__(self, finished, codes):
        self.finished = finished
        self.codes = codes

        self.remaining = 1024 * 10
        self.data = ""

    def dataReceived(self, bytes):
        if self.remaining:
            chunk = bytes[:self.remaining]

            log.debug('Some data received:')
            log.debug(chunk)

            self.data += chunk
            self.remaining -= len(display)

    def connectionLost(self, reason):
        log.debug('Finished receiving body:', reason.getErrorMessage())

        lines = re.split("\n", self.data)
        data = lines[2:-1] # 1st 2 lines is header
        parsed = (re.split("\|", i) for i in data)
        interesting = ((i[3],i[4]) for i in parsed if i[3] in self.codes)

        self.finished.callback(interesting)

class MainController(controller.CementBaseController):
    class Meta:
        description = 'PyCNB entry point'

    @controller.expose()
    def default(self):
        agent = Agent(reactor)
        url = 'http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt'

        d = agent.request(
            'GET',
            url,
            Headers({'User-Agent': ['Twisted Web Client Example']}))

        d2 = Deferred()

        d.addCallback(lambda response: response.deliverBody(DailyRatesProtocol(d2, ["EUR", "USD"])))
        d.addErrback(d2.errback)

        d2.addCallback(self._gotRates)
        d.addErrback(log.error)
        d.addBoth(lambda x: reactor.stop())

        reactor.run()

    def _gotRates(self, rates):
        [pprint(x) for x in rates]
