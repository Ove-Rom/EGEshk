def f(a, b, n):
    if a + b >= 65: return n % 2 == 0
    if n == 0: return 0
    h = [f(a + 1, b, n - 1), f(a, b + 1, n - 1),
         f(a * 3, b, n - 1), f(a, b * 3, n - 1)]
    return all(h) if n % 2 == 0 else any(h)

def f19(a, b, n):
    if a + b >= 65: return n % 2 == 0
    if n == 0: return 0
    h = [f19(a + 1, b, n - 1), f19(a, b + 1, n - 1),
         f19(a * 3, b, n - 1), f19(a, b * 3, n - 1)]
    return any(h)

print("19)", *[a for a in range(1, 59) if f19(a, 6, 2)])
print("20)", *[a for a in range(1, 59) if f(a, 6, 3) and not f(a, 6, 1)])
print("21)", *[a for a in range(1, 59) if f(a, 6, 4) and not f(a, 6, 2)])