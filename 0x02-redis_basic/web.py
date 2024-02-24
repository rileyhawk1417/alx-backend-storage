#!/usr/bin/env python3
"""
Module to interact with redis.
To cache & Track
"""

import redis
import requests
from functools import wraps
from typing import Callable

redis_store = redis.Redis()


def cache_data(method: Callable) -> Callable:
    """
    Cache the output of fetched data.
    """
    @wraps(method)
    def invoker(url) -> str:
        """
        Wrapper to cache the output
        """
        redis_store.incr(f'count:{url}')
        res = redis_store.get(f'result:{url}')
        if res:
            return res.decode('utf-8')
        res = method(url)
        redis_store.set(f'count:{url}', 0)
        redis_store.setex(f'result:{url}', 10, res)
        return res
    return invoker


@cache_data
def get_page(url: str) -> str:
    """
    Args:
        url: (str) Url to fetch data
    Return:
        request.body: Return request text
    """
    return requests.get(url).text
