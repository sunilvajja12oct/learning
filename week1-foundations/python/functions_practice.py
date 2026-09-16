#!/usr/bin/env python3

def check_server_health(server,healthy_status=200):
    return server['status'] == healthy_status


def summarize_servers(servers):
    healthy_count = 0
    
    for server in servers:
        if check_server_health(server):
            print(f"OK: {server['name']}")
            healthy_count += 1
        elif server['status'] == 404:
            print(f"NOT FOUND: {server['name']}")
        else:
            print(f"FAIL: {server['name']} (status {server['status']})")
    return healthy_count



if __name__ == "__main__":
    servers = [
        {"name": "web-01", "status": 200},
        {"name": "web-02", "status": 500},
        {"name": "db-01", "status": 200},
        {"name": "cache-01", "status":404},
    ]
    count = summarize_servers(servers)
    print(f"\n{count} out of {len(servers)} servers healthy")