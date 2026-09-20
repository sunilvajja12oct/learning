#!/usr/bin/env python3

class Server:
    def __init__(self, name, status, region = "us-east-1"):
        self.name = name
        self.status = status
        self.region = region

    def is_healthy(self):
        return self.status == 200

    def describe(self):
        state = "healthy" if self.is_healthy() else "unhealthy"
        return f"{self.name} ({self.region}) is {state}"