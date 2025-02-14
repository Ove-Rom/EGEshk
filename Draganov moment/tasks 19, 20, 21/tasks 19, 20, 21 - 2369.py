def f(a, b, c, n):
    if a + b + c >= 73: return n % 2 == 0
    if n == 0: return 0
    h = [f(a + 3, b, c, n - 1), f(a, b + 3, c, n - 1), f(a, b, c + 3, n - 1),
        f(a + 13, b, c, n - 1), f(a, b + 13, c, n - 1), f(a, b, c + 13, n - 1),
        f(a + 23, b, c, n - 1), f(a, b + 23, c, n - 1), f(a, b, c + 23, n - 1)]
    return all(h) if n % 2 == 0 else any(h)

def f2(a, b, c, n):
    if a + b + c >= 73: return n % 2 == 0
    if n == 0: return 0
    h = [f(a + 3, b, c, n - 1), f(a, b + 3, c, n - 1), f(a, b, c + 3, n - 1),
        f(a + 13, b, c, n - 1), f(a, b + 13, c, n - 1), f(a, b, c + 13, n - 1),
        f(a + 23, b, c, n - 1), f(a, b + 23, c, n - 1), f(a, b, c + 23, n - 1)]
    return any(h)


print("19)", *[s for s in range(2, 23) if f2(2, s, 2*s, 2)])
print("20)", *[s for s in range(2, 23) if f(2, s, 2*s, 3) and not f(2, s, 2*s, 1)])
print("21)", *[s for s in range(2, 23) if f(2, s, 2*s, 4) and not f(2, s, 2*s,2)])
