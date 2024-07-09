#!/usr/bin/env python3
"""Async Comprehensions Module"""

from asyncio import gather
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Calculate runtime for 4 parallel jobs"""
    start = time()
    jobs = [async_comprehension() for _ in range(4)]
    await gather(*jobs)
    end = time()
    return (end - start)
