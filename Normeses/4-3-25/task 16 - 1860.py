from functools import lru_cache


@lru_cache(None)
def f(n):
    if n <= 1:
        return 0
    elif n > 1 and n % 2:
        return f(n - 1) + 3 * n ** 2
    elif n > 1 and n % 2 == 0:
        return n // 2 + f(n - 1) + 2

for i in range(50): f(i)

print(f(49))