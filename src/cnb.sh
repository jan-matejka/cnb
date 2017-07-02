#! /usr/bin/env zsh

SELF="${0##*/}"

cmd=$SELF-${1:?"Missing argument command"}
shift
xdgenv-exec CNB cnb -- $cmd "$@"
