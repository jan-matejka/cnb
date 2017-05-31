#! /usr/bin/env zsh

SELF="${0##*/}"
. cnb-prelude

# XDG Base Directory Specification v0.8
export CNB_CACHE=${CNB_CACHE:-${XDG_CACHE_HOME:-${HOME}/.cache}/cnb}
export CNB_CONFIG=${CNB_CONFIG:-${XDG_CONFIG_HOME:-${HOME}/.config}/cnb}
export CNB_URL=${CNB_URL:-https://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt}

export CNB_LOCAL_RATES=${CNB_CACHE}/rates

cmd-dispatch "$@"
