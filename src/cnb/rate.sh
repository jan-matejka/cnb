#! /usr/bin/env zsh

SELF="${0##*/}"
. cnb-prelude

check-arg currency ${1:-}
c=$1

cnb fetch || {
  if ! test -f $CNB_LOCAL_RATES; then
    fatal "local-rates not cached yet"
  else
    e-msg "using cached local-rates from %s" "$(date -r $CNB_LOCAL_RATES)"
  fi
}

ln=$(grep -s $c ${CNB_LOCAL_RATES}) || fatal "Invalid currency %s" $c

ln=(${(s:|:)ln})

echo ${ln[3]} ${ln[5]/,/.}
