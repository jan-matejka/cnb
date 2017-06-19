CNB
###

http://cnb.cz daily rates in your command line
----------------------------------------------

:Manual section: 1
:Date: 2017-06-03
:Author: Jan Matějka yac@blesmrt.net
:Manual group: cnb manual

SYNOPSIS
========

  cnb <command> [<args>]

DESCRIPTION
===========

Access and convert currency rates from / to CZK from your command line.

``local-rates`` (``man 1 cnb-path``) file is cached and refreshed
when its modification time is older than an hour.

Commands using the ``local-rates`` print an error if its refresh fails but
proceeds as usual to allow for off-line use if ``local-rates`` exists.

COMMANDS
========

* ``man 1 cnb-fetch``

* ``man 1 cnb-from``

* ``man 1 cnb-rate``

* ``man 1 cnb-to``

* ``man 1 cnb-fetch``

* ``man 1 cnb-path``


ENVIRONMENT VARIABLES
=====================

XDG_CACHE_HOME
  as defined by
  `XDG Base Directory Specification v0.8 <https://standards.freedesktop.org/basedir-spec/basedir-spec-0.8.html>`__

CNB_CACHE
  overrides XDG_CACHE_HOME for cnb

CNB_URL
  URL to download the daily rates txt file from

BUILD & INSTALLATION
====================

::

  $ make
  $ make check
  $ make install

DEPENDENCIES
============

Build
+++++

* python-docutils

* GNU make

Tests
+++++

* ``cram <https://github.com/brodie/cram>``

Runtime
+++++++

* zsh

* coreutils

* curl

.. include:: common-foot.rst
