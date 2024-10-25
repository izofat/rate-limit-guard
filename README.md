# Rate Limiting Decorator

This Python module provides a `rate_limit_decorator` that allows you to limit the rate at which a function can be called. It supports both synchronous and asynchronous functions, making it versatile for various applications.

## Installation

Install the rate-limit-guard package via pip:

```bash
pip install rate-limit-guard
```

Once installed, import rate_limit_decorator into your project and apply it to your functions to enable rate limiting.

## Features

- **Rate Limiting**: Control the maximum number of function calls within a given time interval.
- **Support for Asynchronous and Synchronous Functions**: The decorator works seamlessly with both types of functions.
- **Easy Integration**: Simply apply the decorator to your function, and it will handle rate limiting for you.

## Usage

Here’s a basic example of how to use the `rate_limit_decorator`:

### Synchronous

```python
from rate_limit_guard import rate_limit_decorator

@rate_limit_decorator(interval=1, max_calls=5)
def my_function():
    print("Function is called")

def main():
    try:
        for _ in range(10):
            my_function()
    except RuntimeError:
        # this will be raised after the rate limit is reached
        pass
```

### Asynchronous

```python
from rate_limit_guard import rate_limit_decorator
import asyncio

@rate_limit_decorator(interval=1, max_calls=5)
async def my_async_function():
    print("Async function is called")
    await asyncio.sleep(0.5)

async def main():
    try:
        for _ in range(10):
            await my_async_function()
    except RuntimeError:
        # this will be raised after the rate limit is reached
        pass
```
