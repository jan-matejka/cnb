#!/bin/false
# vim: filetype=zsh

setopt no_unset
setopt pipe_fail
setopt warn_create_global

function fatal {
  f-msg "$@"
  exit 1
}

function msg {
  local level=$1
  local msg=$2
  shift 2
  msg=$(printf $msg "$@")
  printf >&2 -- "%s: %s: %s\n" $SELF $level $msg
}

function f-msg {
  msg fatal "$@"
}

function e-msg {
  msg error "$@"
}

function f-already-exists {
  fatal "%s %s already exists" "$@"
}

function check-arg {
  test -z "${2:-}" && fatal "missing argument %s" $1
}

function check-executable {
  type "$1" >/dev/null 2>&1 || fatal "cannot execute %s" $1
}

function cmd-dispatch {
  check-arg "command" ${1:-}

  local cmd=$SELF-$1
  shift

  check-executable $cmd
  exec $cmd "$@"
}
