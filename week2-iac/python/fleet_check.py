#!/usr/bin/env python3

from server import Server

fleet = [
    Server("web-01", 200),
    Server("web-02", 500),
    Server("db-01", 200, region="us-west-2")
]

healthy_count = sum(1 for s in fleet if s.is_healthy())

for s in fleet:
    print(s.describe())

print(f"\n{healthy_count} out of {len(fleet)} servers healthy")

if __name__ == "__main__":
    pass