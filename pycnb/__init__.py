#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from .controller import getRates

class Wrapper(object):
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.drp = None

    def set_drp(self, drp):
        self.drp = drp

    def __getattr__(self, name):
        try:
            return getattr(self.wrapped, name)
        except AttributeError:
            if not self.drp:
                getRates(self.set_drp)
            return self.drp.rates[name]

sys.modules[__name__] = Wrapper(sys.modules[__name__])
