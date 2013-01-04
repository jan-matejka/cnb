#! /usr/bin/env python
# -*- coding: utf-8 -*-

from pycnb.controller import getRates
import sys

class Wrapper(object):
    def __init__(self):
        getRates(self.set_drp)

    def set_drp(self, drp):
        self.drp = drp

    def __getattr__(self, name):
        return self.drp.rates[name]

sys.modules[__name__] = Wrapper()
