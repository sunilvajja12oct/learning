#! /bin/bash

URL="http://localhost:8080/helth"
RETRIES=0
MAX_RETRIES=5

until curl -s -o /dev/null -f "$URL"; do
	RETRIES=$((RETRIES+1))
	if [ $RETRIES -ge $MAX_RETRIES ]; then
		echo "Server did not come up after $MAX_RETRIES attempts"
		exit 1
	fi
	echo "Waiting for $URL...retry $RETRIES"
	sleep 5
done
echo "$URL is up"
