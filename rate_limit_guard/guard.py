"""
This module contains the RateLimitGuard class,
which is used to rate limit the number of calls to a function.

You don't need to import this class rate_limit_decorator handles everything for you.
"""

import asyncio
import time
from typing import Optional


class RateLimitGuard:
    """
    A class that rate limits the number of calls to a function.

    :param interval: The time interval in seconds.
    :param max_calls: The maximum number of calls allowed within the interval.
    """

    def __init__(self, interval: int = 0, max_calls: Optional[int] = None):
        self.interval = interval
        self.last_call_time = 0
        self.count = 0
        self.max_calls = max_calls

    @property
    def time_to_sleep(self):
        if self.interval is None:
            return 0

        elapsed = time.time() - self.last_call_time
        if elapsed < self.interval:
            print(f"Sleeping for {self.interval - elapsed:.2f} seconds")
            return self.interval - elapsed
        return 0

    async def sleep_async(self):
        await asyncio.sleep(self.time_to_sleep)

        self.last_call_time = time.time()

    def sleep_sync(self):
        time.sleep(self.time_to_sleep)

        self.last_call_time = time.time()

    def step(self):
        if self.max_calls is None:
            return True

        if self.max_calls == self.count:
            return False

        self.count += 1
        return True
