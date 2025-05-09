from math import ceil


def f(a, b, n):
    if (a + b) <= 72: return n % 2 == 0
    if n == 0: return 0
    h = [f(a - 3, b, n - 1), f(ceil(a / 2), b, n - 1),
         f(a, b - 3, n - 1), f(a, ceil(b / 2), n - 1)]
    return all(h) if n % 2 == 0 else any(h)

def f19(a, b, n):
    if (a + b) <= 72: return n % 2 == 0
    if n == 0: return 0
    h = [f19(a - 3, b, n - 1), f19(ceil(a / 2), b, n - 1),
         f19(a, b - 3, n - 1), f19(a, ceil(b / 2), n - 1)]
    return any(h)

print("19)", *[a for a in range(23, 1_000) if f19(a, 50, 2)])
print("20)", *[a for a in range(23, 1_000) if f(a, 50, 3) and not f(a, 50, 1)])
print("21)", *[a for a in range(23, 1_000) if f(a, 50, 4) and not f(a, 50, 2)])