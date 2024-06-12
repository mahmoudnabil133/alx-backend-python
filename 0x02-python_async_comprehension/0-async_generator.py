#!/usr/bin/env python3
"generator that asynchronously yields random numbers between 0 and 10"
from typing import Generator
import random
import asyncio


async def async_generator() -> Generator[float, None, None]:
    "generator that asynchronously yields random numbers between 0 and 10"
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
