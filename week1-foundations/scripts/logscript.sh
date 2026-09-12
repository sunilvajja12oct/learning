#!/bin/bash

LOGFILE="/mnt/d/logs/myapp/log"
MAXSIZE=1048576 #1MB

if [ -f "$LOGFILE" ] && [ $(stat -c%s "$LOGFILE") -ge $MAXSIZE ]; then
	mv "$LOGFILE" "$LOGFILE.$(date +%Y%m%d%H%M%S)"
	touch "$LOGFILE"
	echo "Rotated log file"
else
	echo "File not found"
fi
