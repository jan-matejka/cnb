setup 0
=======

  $ export HOME=$(pwd)/home

  $ export LOCAL=$(cnb path local-rates)
  $ test -f $LOCAL
  [1]

  $ export SRC="$(pwd)/fake-src"
  $ export CNB_URL="file://${SRC}"
  $ echo "foo" >> $SRC
  $ cat $SRC
  foo

fetch first
===========

  $ cnb fetch
  $ test -f $LOCAL
  $ cat $LOCAL
  foo

setup 1
=======

  $ touch -d "2 hours ago" $LOCAL
  $ echo "bar" > $SRC

fetch when expired
==================

  $ cnb fetch
  $ cat $LOCAL
  bar

setup 2
=======

  $ echo "foo" > $SRC

fetch noops if not expired
==========================

  $ cnb fetch
  $ cat $LOCAL
  bar

fetch fail
==========

  $ export CNB_URL="http://example.invalid"
  $ rm $(cnb path local-rates)
  $ cnb fetch
  curl: (6) Could not resolve host: example.invalid
  cnb-fetch: fatal: curl failed
  [1]
