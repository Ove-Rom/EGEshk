from functools import lru_cache
from sys import setrecursionlimit



@lru_cache(None)
def f(a, b, c=None):
    if a == b: return 1
    if a > b or a == c: return 0
    return (f(a + 3, b, c) +
            f(a + 5, b, c) +
            f(a * 2, b, c)) % 1_000_000

for i in range(3_000, 0, -1): f(i, 3_000)
for i in range(10_000, 3_000, -1): f(i, 10_000, 5_000)
for i in range(5_000, 1, -1): f(i, 5_000, 3_000)
for i in range(10_000, 5_000, -1): f(i, 10_000)

print((f(1, 3_000) * f(3_000, 10_000, 5_000) + \
      f(1, 5_000, 3_000) * f(5_000, 10_000)) % 1_000_000)


# setrecursionlimit(10**5)
#
# # @lru_cache(None)
# def f(a, b):
#     if a == b: return 1
#     if a > b: return 0
#     return (f(a + 3, b) +
#             f(a + 5, b) +
#             f(a * 2, b))
#
# r = - 2 * f(1, 3000) * f(3000, 5000) * f(5000, 10000) \
#     + f(1, 3000) + f(3000, 10000) + f(1, 5000) * f(5000, 10000)
#
# print(str(f)[-6:])