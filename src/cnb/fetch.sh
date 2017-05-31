#! /usr/bin/env zsh

SELF="${0##*/}"
. cnb-prelude

if [[ -f $CNB_LOCAL_RATES && $(( $(date +%s) - $(date -r $CNB_LOCAL_RATES +%s) )) -lt 3600 ]] ; then
    return
fi

mkdir -p $(dirname $CNB_LOCAL_RATES)
curl -s --show-error $CNB_URL -o $CNB_LOCAL_RATES || fatal "curl failed"
