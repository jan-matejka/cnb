#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from pprint import pprint
import code
from decimal import Decimal
import readline
from rlcompleter import Completer

from cement.core import foundation, handler, controller
from twisted.internet import reactor

from .protocol import get_rates

class MainController(controller.CementBaseController):
    class Meta:
        description = 'PyCNB entry point'
        arguments = [
            (['-i', '--interactive'], dict(action='store_true')),
        ]

    def get_callbacks(self):
        if self.pargs.interactive:
            return [self.create_namespace, self.interact]
        else:
            return [self.print_all]

    @controller.expose()
    def default(self):
        d = get_rates(reactor)
        for cb in self.get_callbacks():
            d.addCallback(cb)

        d.addBoth(lambda x: reactor.stop())
        reactor.run()

    def create_namespace(self, ns):
        ns['D'] = Decimal
        return ns

    def interact(self, ns):
        c = Completer(ns)
        readline.set_completer(c.complete)
        readline.parse_and_bind("tab: complete")
        code.interact(local=ns)

    def print_all(self, rates):
        for c,r in rates.items():
            print("{currency} {rate}".format(currency=c, rate=r))

class PyCNBApp(foundation.CementApp):
    class Meta:
        label = 'pycnb'
        base_controller = MainController

def main():
    app = PyCNBApp()
    app.setup()
    app.run()
