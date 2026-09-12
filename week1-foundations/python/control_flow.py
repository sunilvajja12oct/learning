#!/usr/bin/env python3

servers = [
    {"name": "web-01", "status": 200},
    {"name": "web-02", "status": 500},
    {"name": "db-01", "status": 200},
    {"name": "cache-01", "status": 404},
]

health_count = 0

for server in servers:
    name = server["name"]
    status = server["status"]

    if status == 200:
        print(f"OK: {name}")
        health_count += 1
    elif status == 404:
        print(f"NOT FOUND: {name}")
        continue
    else:
        print(f"FAIL : {name} (status {status})")

print(f"\n{health_count} out of {len(servers)} servers healthy")
