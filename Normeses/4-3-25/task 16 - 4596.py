from functools import lru_cache


@lru_cache(None)
def f(n):
    if n < 3:
        return 1
    elif n > 2 and n % 2 == 0:
        return f(n - 1) + n - 1
    elif n > 2 and n % 2:
        return f(n - 2) + 2 * n

for i in range(35): f(i)

print(f(34))