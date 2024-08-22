import time

import pytest
from requests import request

from rate_limit_guard import rate_limit_decorator

from .config import INTERVAL, MAX_CALLS


@rate_limit_decorator(interval=INTERVAL, max_calls=MAX_CALLS)
def create_request_sync(request_url):
    req = request("GET", url=request_url, timeout=INTERVAL)
    return req.json()


def test_interval_sync(url):
    start = time.time()
    for _ in range(MAX_CALLS):
        create_request_sync(url)
    end = time.time()

    assert end - start > INTERVAL * (MAX_CALLS - 1)  # this can fail in slow connections
    assert end - start < INTERVAL * MAX_CALLS


def test_max_calls_sync(url):
    try:
        for _ in range(1):
            create_request_sync(url)
    except StopIteration:
        assert True
    else:
        pytest.fail("StopIteration not raised")
