#! /usr/bin/env zsh

SELF="${0##*/}"

cmd=${1:-}
[[ -n ${cmd} ]] || {
  printf >&2 "%s: fatal: missing argument command\n" $SELF
  exit 1
}
cmd=$SELF-$cmd
shift
xdgenv-exec CNB cnb -- $cmd "$@"
