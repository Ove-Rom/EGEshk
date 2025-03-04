from functools import reduce
from operator import mul

def div(x):
    ans = set()
    for i in range(1, round(x ** .5) + 1):
        if x % i == 0:
            ans |= {i, x // i}
    if len(ans) > 10:
        s = sum(ans)
        m = reduce(mul, ans)
        if s % 2 == m % 2 == 1: return len(ans)
    return 0

c = 0

for i in range(800_001, 10**10):
    d = div(i)
    if d:
        print(i, d)
        c += 1
        if c == 6: break