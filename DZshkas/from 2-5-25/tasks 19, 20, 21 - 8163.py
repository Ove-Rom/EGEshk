def f(a, n):
    if a >= 348: return n % 2 == 0
    if n == 0: return 0
    h = [f(a + 3, n - 1), f(a * 3, n - 1)]
    return all(h) if n % 2 == 0 else any(h)


def f19(a, n):
    if a >= 348: return n % 2 == 0
    if n == 0: return 0
    h = [f19(a + 3, n - 1), f19(a * 3, n - 1)]
    return any(h)


print("19)", *[a for a in range(1, 348) if f19(a, 2)])
print("20)", *[a for a in range(1, 348) if f(a, 3) and not f(a, 1)])
print("21)", *[a for a in range(1, 348) if f(a, 4) and not f(a, 2)])
