import time

import pytest
from aiohttp import ClientSession

from rate_limit_guard import rate_limit_decorator

from .config import INTERVAL, MAX_CALLS


@rate_limit_decorator(interval=INTERVAL, max_calls=MAX_CALLS)
async def create_request_async(request_url):
    async with ClientSession() as session:
        async with session.get(request_url) as response:
            return await response.json()


@pytest.mark.asyncio
async def test_interval_async(url):
    start = time.time()
    for _ in range(MAX_CALLS):
        await create_request_async(url)
    end = time.time()

    assert end - start > INTERVAL * (MAX_CALLS - 1)  # this can fail in slow connections
    assert end - start < INTERVAL * MAX_CALLS


@pytest.mark.asyncio
async def test_max_calls_async(url):
    try:
        for _ in range(1):
            await create_request_async(url)
    except RuntimeError:
        assert True
    else:
        pytest.fail("StopIteration not raised")
