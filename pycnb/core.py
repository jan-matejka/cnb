#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
log = logging.getLogger(__name__)

from cement.core import foundation, handler, hook
from . import controller as ctrl

class PyCNBApp(foundation.CementApp):
    class Meta:
        label = 'pycnb'
        base_controller = ctrl.MainController

def main():
    app = PyCNBApp()
    app.setup()
    app.run()
