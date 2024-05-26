setup 0
=======

  $ . ${TESTDIR}/setup

  $ export CNB_URL="file://${TESTDIR}/rates.txt"

rate
====

  $ cnb rate USD
  1 23.545

  $ cnb rate GBP
  1 30.239

  $ cnb rate JPY
  100 21.237

invalid currency
================

  $ cnb rate FOO 10
  cnb-rate: fatal: Invalid currency FOO
  [1]

to conversion
=============

  $ cnb to USD 100
  4.25

  $ cnb to JPY 100
  470.88

from conversion
===============

  $ cnb from USD 4.2471862391165853
  100.00

  $ cnb from JPY 470.87630079578099
  100.00

large numbers
=============

  $ cnb to JPY 100000000
  470876300.80

invalid currency
================

  $ cnb to FOO 10
  cnb-rate: fatal: Invalid currency FOO
  [1]

conversions fallback to using expired local-rates
=================================================

  $ touch -d @1496370050 $(cnb path local-rates)
  $ export CNB_URL="http://example.invalid"
  $ cnb to USD 100
  curl: (6) Could not resolve host: example.invalid
  cnb-fetch: fatal: curl failed
  cnb-rate: error: using cached local-rates from Fri Jun  2 02:20:50 UTC 2017
  4.25

fetch fail without local-rates
==============================

  $ rm $(cnb path local-rates)
  $ export CNB_URL="http://example.invalid"
  $ cnb to USD 100
  curl: (6) Could not resolve host: example.invalid
  cnb-fetch: fatal: curl failed
  cnb-rate: fatal: local-rates not cached yet
  [1]

invalid argv
============

  $ cnb rate
  cnb-rate: fatal: missing argument currency
  [1]

  $ cnb to
  cnb-to: fatal: missing argument currency
  [1]

  $ cnb to FOO
  cnb-to: fatal: missing argument amount
  [1]

  $ cnb from
  cnb-from: fatal: missing argument currency
  [1]

  $ cnb from FOO
  cnb-from: fatal: missing argument amount
  [1]
