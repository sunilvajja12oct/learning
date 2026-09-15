#!/bin/bash

URL="http://localhost:8000/health"
STATUS=$(curl -s -o /dev/null -w "%{http_code}" $URL)

if [ "$STATUS" -eq 200 ]; then
	echo "OK: $URL is up(status $STATUS)"
	exit 0
else
	echo "FAIL: $URL returned status $STATUS"
	exit 1
fi
