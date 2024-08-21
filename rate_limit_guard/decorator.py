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

from functools import wraps
from typing import Optional

from rate_limit_guard.guard import RateLimitGuard


def rate_limit_decorator(
    interval: Optional[int] = None, max_calls: Optional[int] = None
):
    """
    A decorator that limits the rate at which a function can be called.

    :param interval: The time interval in seconds.
    :param max_calls: The maximum number of calls allowed within the interval.
    :return: A decorator function.

    :raises StopIteration: If the rate limit is exceeded.
    """
    guard = RateLimitGuard(interval, max_calls)

    def decorator(func):

        @wraps(func)
        async def wrapper(*args, **kwargs):
            nonlocal guard

            if not guard.step():
                raise StopIteration("Rate limit exceeded")

            await guard.sleep()
            return await func(*args, **kwargs)

        return wrapper

    return decorator
