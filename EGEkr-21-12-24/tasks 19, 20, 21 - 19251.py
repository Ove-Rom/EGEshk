from functools import lru_cache

# 41
# 14 35
# 32

def H(s):
    return s + 3, s + 6, s * 3

@lru_cache(None)
def f(p):
    n = p
    if n >= 132: return 'L', 0
    if any(f(h)[0] == 'L' for h in H(p)): return 'W', 1 + min(f(h)[1] for h in H(p) if f(h)[0] == 'L')
    return 'L', 1 + max(f(h)[1] for h in H(p))

for p in range(132, 0, -1):
    print(p, f(p))
