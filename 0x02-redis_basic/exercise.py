#!/usr/bin/env python3

"""Module showcases the use of caching in redis"""
from functools import wraps
from typing import Callable, Optional, Union, Any
import redis
import uuid


def count_calls(method: Callable) -> Callable:
    """Decorate store method in Cache class"""

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """Wrapper to count the number of
        times a redis function is triggered
        """
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Track call history for inputs & outputs of a function
    """
    @wraps(method)
    def summoner(self, *args, **kwargs) -> Any:
        """Return method output after saving the history"""
        _inputs = f"{method.__qualname__}:inputs"
        _outputs = f"{method.__qualname__}:outputs"
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(_inputs, str(args))
        res = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(_outputs, res)
        return res
    return summoner


def replay(method: Callable) -> None:
    """Display function call history"""
    if method is None or not hasattr(method, '__self__'):
        return
    store = getattr(method.__self__, '_redis', None)
    if not isinstance(store, redis.Redis):
        return
    fn = method.__qualname__
    _inputs = f"{fn}:inputs"
    _outputs = f"{fn}:outputs"
    fn_count = 0
    if store.exists(fn) != 0:
        fn_count = int(store.get(fn))
    print(f"{fn} was called {fn_count} times:")
    fn_inputs = store.lrange(_inputs, 0, -1)
    fn_outputs = store.lrange(_outputs, 0, -1)
    for fn_inputs, fn_outputs in zip(fn_inputs, fn_outputs):
        print("{}(*{}) -> {}".format(
            fn,
            fn_inputs.decode("utf-8"),
            fn_outputs
        ))


class Cache():
    """Initiate a Redis Instance"""

    def __init__(self) -> None:
        """Init a redis instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the key/value in redis"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Get value using key in redis"""
        res = self._redis.get(key)
        if res is not None and fn is not None:
            return fn(res)
        # Well the linter is throwing an error but the function works
        return res

    def get_str(self, key: str) -> Optional[str]:
        """Decode string to utf-8"""
        # Well the linter is throwing an error but the function works
        return self.get(key, fn=lambda d: d.decode('utf-8') if d else None)

    def get_int(self, key: str) -> Optional[int]:
        """Get an int type of the data"""
        # Well the linter is throwing an error but the function works
        return self.get(key, fn=lambda d: int(d) if d else None)
