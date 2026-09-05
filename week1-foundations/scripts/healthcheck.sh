#!/bin/bash

URL="https://www.example.com"
STATUS=$(curl -s -o /dev/null -w "%{http_code}" $URL)

if [ "$STATUS" -eq 200 ]; then
	echo "OK: $UTL is up(status $STATUS)"
	exit 0
else
	echo "FAIL: $URL returned status $STATUS"
	exit 1
fi
