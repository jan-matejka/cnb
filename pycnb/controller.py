#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
log = logging.getLogger(__name__)
# log commented out because it breaks

from cement.core import foundation, controller, handler
from pprint import pprint
from decimal import Decimal

from twisted.internet import reactor
from twisted.web.client import Agent
from twisted.web.http_headers import Headers
from twisted.internet import defer
from twisted.internet.protocol import Protocol
from twisted.protocols.basic import LineReceiver

class DailyRatesProtocol(LineReceiver):
    delimiter = '\n'

    def __init__(self):
        self.deferred = defer.Deferred()

        self.line_no = 0
        self.rates = {}

    def lineReceived(self, line):
        if self.line_no < 2:
            # 1st 2 lines is header
            self.line_no += 1
            return

        cols = line.split("|")
        self.rates[cols[3]] = Decimal(cols[4].replace(',', '.'))

    def connectionLost(self, reason):
        self.deferred.callback(self)

def getRates(cb):
    agent = Agent(reactor)
    url = 'http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt'

    d = agent.request(
        'GET',
        url,
        Headers({'User-Agent': ['Twisted Web Client Example']}))

    drp = DailyRatesProtocol()
    drp.deferred.addCallback(cb)

    d.addCallback(lambda r: r.deliverBody(drp))
    d.addCallback(lambda _: drp.deferred)
    d.addErrback(log.error)
    d.addBoth(lambda x: reactor.stop())

    reactor.run()

class MainController(controller.CementBaseController):
    class Meta:
        description = 'PyCNB entry point'

    @controller.expose()
    def default(self):
        getRates(self._gotRates)

    def _gotRates(self, drp):
        [pprint(i) for i in drp.rates.items()
            if i[0] in ["EUR", "USD"]]

