#!/bin/bash
# Setze das Limit für offene Dateien
ulimit -n 65536

# Starte Fluentd mit den übergebenen Argumenten
exec /usr/local/bin/fluentd "$@"