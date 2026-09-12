#!/bin/bash

while IFS= read -r URL; do
	STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$URL")
	if [ "$STATUS" -eq 200 ]; then
		echo "OK: $URL ($STATUS)"
	else
		echo "FAIL: $URL ($STATUS)"
	fi
done < urls.txt
