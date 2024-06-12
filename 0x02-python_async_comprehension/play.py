#!/usr/bin/env python3
from typing import Generator

import asyncio
async def gen():
    for i in range(100):
        await asyncio.sleep(.3)
        yield i

async def main():
    async for i in gen():
        print(i)

asyncio.run(main())
