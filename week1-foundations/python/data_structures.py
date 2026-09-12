#!/usr/bin/env python3

servers = [
    {"name": "web-01", "region": "us-east-1", "status": 200},
    {"name": "web-02", "region": "us-west-2", "status": 500},
    {"name": "db-01", "region": "us-east-1", "status": 200},
]

# List comprehension: names of only the healthy servers
healthy_names = [s["name"] for s in servers if s["status"] == 200]
print(f" Healthy Servers: {healthy_names}")

# Dictionary: count servers per region
region_counts = {}
for s in servers:
    region = s["region"]
    region_counts[region] = region_counts.get(region, 0) +1

print(f"Server per region: {region_counts}")

# Set: unique regions in use
unique_regions = {s["region"] for s in servers}
print(f"Unique regions: {unique_regions}")