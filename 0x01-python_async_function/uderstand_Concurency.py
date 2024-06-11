#!/usr/bin/env python3
import asyncio
import time
async def say_hello():
    print("Hello!")
    await asyncio.sleep(.1)  # Simulate an I/O operation
    print("World!")

async def say_bye():
    print("Goodbye!")
    await asyncio.sleep(1)  # Simulate another I/O operation
    print("See you!")

async def main():
    task1 = asyncio.create_task(say_hello())  # Create the first task
    task2 = asyncio.create_task(say_bye())    # Create the second task
    await task1  # Wait for the first task to complete
    await task2  # Wait for the second task to complete
    print('haha')

# Run the main function
asyncio.run(main())
