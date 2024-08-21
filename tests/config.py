import toml

config = toml.load("./config.toml")

TEST_URL = config.get("test_url")

TEST_ENDPOINTS = config.get("test_endpoints")

INTERVAL = config.get("interval")

MAX_CALLS = config.get("max_calls")
