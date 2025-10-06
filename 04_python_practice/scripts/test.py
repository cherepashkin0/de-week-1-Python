def memoize(fn):
    """Decorator caching fn(x) for hashable x."""
    cache = {}
    def wrapper(*args, **kwargs):
        key = (args, tuple(kwargs.items()))
        if key not in cache:
            cache[key] = fn(*args, **kwargs)
        return cache[key]
    return wrapper

calls = {"n": 0}


@memoize
def square(x):
    calls["n"] += 1
    return x*x

x = 10
print(square(x))