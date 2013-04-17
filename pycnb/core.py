#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import logging
log = logging.getLogger(__name__)

from cement.core import foundation, handler, controller
from pprint import pprint
from .protocol import get_rates
from twisted.internet import reactor

class MainController(controller.CementBaseController):
    class Meta:
        description = 'PyCNB entry point'

    @controller.expose()
    def default(self):
        d = get_rates(self._gotRates, reactor)
        d.addBoth(lambda x: reactor.stop())
        reactor.run()

    def _gotRates(self, rates):
        [print("{0} {1}".format(*i)) for i in rates.items()]

class PyCNBApp(foundation.CementApp):
    class Meta:
        label = 'pycnb'
        base_controller = MainController

def main():
    app = PyCNBApp()
    app.setup()
    app.run()
