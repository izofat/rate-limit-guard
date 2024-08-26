"""
This module contains the rate limit decorator.
Implementing a rate limit decorator is a common use case for the rate limit guard.
The decorator takes two optional arguments: interval and max_calls.
The interval argument specifies the time interval in seconds.
The max_calls argument specifies the maximum number of calls allowed within the interval.
If the rate limit is exceeded, a StopIteration exception is raised.
The decorator uses the RateLimitGuard class to enforce the rate limit.
The RateLimitGuard class keeps track.
You should be ready to handle StopIteration exceptions when using the rate limit decorator.
"""

import inspect
from functools import wraps
from typing import Optional

from rate_limit_guard.guard import RateLimitGuard


def rate_limit_decorator(interval: int = 0, max_calls: Optional[int] = None):
    """
    A decorator that limits the function with given parameters.
    This decorator can be used with both synchronous and asynchronous functions.

    :param interval: The time interval in seconds.
    :param max_calls: The maximum number of calls allowed within the interval.
    :return: A decorator function.

    :raises StopIteration: If the rate limit is exceeded.
    """
    guard = RateLimitGuard(interval, max_calls)

    def decorator(func):
        is_async = inspect.iscoroutinefunction(func)

        @wraps(func)
        async def async_wrapper(*args, **kwargs):
            if not guard.step():
                raise StopIteration("Rate limit exceeded")

            await guard.sleep_async()

            return await func(*args, **kwargs)

        @wraps(func)
        def sync_wrapper(*args, **kwargs):
            if not guard.step():
                raise StopIteration("Rate limit exceeded")

            guard.sleep_sync()

            return func(*args, **kwargs)

        if is_async:
            return async_wrapper
        return sync_wrapper

    return decorator
