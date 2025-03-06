from functools import lru_cache


@lru_cache(None)
def f(n):
    if n < 100:
        return n ** 2
    elif n > 99 and n % 2 == 0:
        return f(n - 1) / 2
    return f(n - 1) * 2


for i in range(16385):
    f(i)

print(1000 * f(16384) / f(7777))
