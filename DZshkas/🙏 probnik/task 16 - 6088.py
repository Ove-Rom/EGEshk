from functools import lru_cache


@lru_cache(None)
def f(n):
    if n > 3_000:
        return 1
    elif n % 2 == 0:
        return f(n + 1) - n + 1
    return f(n + 2) - 2 * n + 2

for i in range(3_002, 33, -1): f(i)

print(2 * f(39) - 2 * f(34))