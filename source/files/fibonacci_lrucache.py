from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n: int) -> int:
    if n == 0:
        return 1
    else:
        value = fibonacci(n - 1) + fibonacci(n - 2)
        return value

print(fibonacci(80))