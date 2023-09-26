"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from collections.abc import Callable


def cache(func: Callable) -> Callable:
    cache_dict = {}

    def wrapper(*args):
        key = tuple(args)
        if key in cache_dict:
            return cache_dict[key]
        else:
            cache_dict[key] = func(*args)
            return cache_dict[key]

    return wrapper
