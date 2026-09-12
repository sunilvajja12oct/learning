#!/usr/bin/env python3

import argparse
import logging
import sys
import boto3 as boto
from botocore.exceptions import ClientError
import json

logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
        )
logger = logging.getLogger(__name__)

def tag_instances(region, key, value):
    ec2 = boto.client("ec2", region_name=region)
    try:
        response = ec2.describe_instances()
        print(json.dumps(response, indent=4, default=str))
    except ClientError as e:
        logger.error(f"Failed to describe instance: {e}")
        sys.exit(1)

    instance_ids = []
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            instance_ids.append(instance["InstanceId"])

    if not instance_ids:
        logger.info("No instnace found in region %s", region)
        return

    try:
        ec2.create_tags(Resources=instance_ids, Tags=[{"Key": key, "Value": value}])
        logger.info("tagged %d instance with %s=%s",len(instance_ids), key, value)
    except ClientError as e:
     logger.error(f"Failed to tag instance: {e}")
     sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Tag all EC2 instnaces in a region")
    parser.add_argument("--region", required=True, help="AWS region, e.g us-east-1")
    parser.add_argument("--key",required=True, help="Tag key")
    parser.add_argument("--value", required=True, help="Tag value")
    args = parser.parse_args()

    tag_instances(args.region, args.key, args.value)

if __name__ == "__main__":
    main()

"""
import time
from botocore.exceptions import ClientError

def describe_with_retry(ec2, max_retries=3):
    for attempt in range(1, max_retries + 1):
        try:
            return ec2.describe_instances()
        except ClientError as e:
            logger.warning("Attempt %d failed: %s", attempt, e)
            if attempt == max_retries:
                logger.error("All retries exhausted")
                raise
            time.sleep(2 ** attempt)  # exponential backoff: 2s, 4s, 8s
"""
