#!/usr/bin/env python3
"0-basic-async"
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    "wait random"
    random_float = random.random() * max_delay

    await asyncio.sleep(random_float)
    return random_float
