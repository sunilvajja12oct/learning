import json

# boto3 returns Python dicts, but you'll often parse raw JSON from files/APIs
with open("config.json") as f:
    config = json.load(f)

region = config.get("region", "us-east-1")  # .get() with default avoids KeyError
