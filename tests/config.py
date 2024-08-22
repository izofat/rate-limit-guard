import os

import toml

if not os.path.exists("./config.toml"):
    raise FileNotFoundError("config.toml not found. Use make config to create one.")

config = toml.load("./config.toml")

TEST_URL = config.get("test_url")

TEST_ENDPOINTS = config.get("test_endpoints")

INTERVAL: int = config.get("interval", 5)

MAX_CALLS = config.get("max_calls", 3)
