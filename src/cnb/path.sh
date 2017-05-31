#! /usr/bin/env zsh

SELF="${0##*/}"
. cnb-prelude


function p-local-rates {
  echo ${CNB_LOCAL_RATES}
}

cmd="p-${1}"
shift
"${cmd}" "$@"
