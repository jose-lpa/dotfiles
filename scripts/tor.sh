#!/usr/bin/env bash

# Tor Network connection script. Tor software must be installed previously.


function usage() {
  echo "usage: $0 start|stop";
  exit 1;
}

function tor_service() {
  launchctl $1 /usr/local/opt/tor/homebrew.mxcl.tor.plist
}

function start() {
  echo "$0: Starting tor service...";
  tor_service load
}

function stop() {
  echo "$0: Stopping tor service...";
  tor_service unload
}

function check() {
  echo "$0: Checking if tor works...";
  if torsocks curl -s https://check.torproject.org | grep -q 'Congratulations. This browser is configured to use Tor.'; then
    echo 'The tor service works';
  else
    echo 'The tor service does NOT work';
  fi
}

case "$1" in
  help|--help|-h)
    usage;;

  start)
    start;;

  stop)
    stop;;

  check)
    check;;

  *)
    echo "error: missing or unrecognized command-line argument";
    usage;;
esac
