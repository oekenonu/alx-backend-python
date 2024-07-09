#!/usr/bin/env python3
"""Async Comprehensions Module"""

from asyncio import sleep
from random import uniform
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Async Comprehensions Function"""
    my_list = [_ async for _ in async_generator()]
    return my_list
