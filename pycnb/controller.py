#! /usr/bin/env python
# -*- coding: utf-8 -*-

import logging
log = logging.getLogger(__name__)

from cement.core import foundation, controller, handler

class MainController(controller.CementBaseController):
    class Meta:
        description = 'PyCNB entry point'

    @controller.expose()
    def default(self):
        print "a"

