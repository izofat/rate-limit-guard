# pylint: disable=redefined-outer-name
import asyncio
import random
import time

import pytest
from aiohttp import ClientSession

from rate_limit_guard import rate_limit_decorator

from .config import INTERVAL, MAX_CALLS, TEST_ENDPOINTS, TEST_URL


@pytest.fixture
def endpoint():
    random_endpoint = random.choice(TEST_ENDPOINTS)
    return TEST_URL + random_endpoint


@pytest.fixture
def index():
    return random.randint(1, 20)


@pytest.fixture
def url(endpoint, index):
    return f"{endpoint}/{index}"


@rate_limit_decorator(interval=INTERVAL, max_calls=MAX_CALLS)
async def create_request(request_url):
    async with ClientSession() as session:
        async with session.get(request_url) as response:
            return await response.json()


@pytest.mark.asyncio
def test_interval(url):
    start = time.time()
    for _ in range(MAX_CALLS):
        asyncio.run(create_request(url))
    end = time.time()

    assert end - start < INTERVAL * MAX_CALLS


@pytest.mark.asyncio
def test_max_calls(url):
    try:
        for _ in range(1):
            asyncio.run(create_request(url))
    except RuntimeError:
        assert True
    else:
        pytest.fail("StopIteration not raised")
