#!/usr/bin/env python3
import json
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

DEFAULT_CONFIG = {"region": "us-east-1", "environment": "dev"}

def load_config(path):
    try:
        with open(path) as f:
            config = json.load(f)
        logger.info("Loaded config from %s", path)
        return config
    except FileNotFoundError:
        logger.warning("Config file %s not found, using defaults", path)
        return DEFAULT_CONFIG
    except json.JSONDecodeError as e:
        logger.error("Config file %s is not valid JSON: %s", path, e)
        raise
    finally:
        logger.info("Finished attempting to load config")

if __name__ == "__main__":
    config = load_config("settings.json")
    print(config)