  $ cnb path local-rates
  /home/*/.cache/cnb/rates (glob)

  $ export XDG_CACHE_HOME=/foo
  $ cnb path local-rates
  /foo/cnb/rates

  $ export CNB_CACHE=/foo
  $ cnb path local-rates
  /foo/rates
