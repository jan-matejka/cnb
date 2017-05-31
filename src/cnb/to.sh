#! /usr/bin/env zsh

SELF="${0##*/}"
. cnb-prelude

check-arg "currency" ${1:-}
currency=$1

check-arg "amount" ${2:-}
amount=$2

rate=$(cnb rate $currency) || exit
rate=(${(s: :)rate})

amount=$(( 1.0 * $amount ))
amount=$(( $amount / ${rate[2]} ))
amount=$(( amount * ${rate[1]} ))

printf "%.*f\n" 2 $amount
