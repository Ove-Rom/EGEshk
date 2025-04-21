def f(a, b, n):
    if (a + b) <= 100: return n % 2 == 0
    if n == 0: return 0
    h = [f(a - 3, b - 3, n - 1),
         f(a // 2, b, n - 1),
         f(a, b // 2, n - 1)]
    return all(h) if n % 2 == 0 else any(h)

def f19(a, b, n):
    if (a + b) <= 100: return n % 2 == 0
    if n == 0: return 0
    h = [f19(a - 3, b - 3, n - 1),
         f19(a // 2, b, n - 1),
         f19(a, b // 2, n - 1)]
    return any(h)

print("19)", *[a for a in range(53, 1_000) if f19(a, 48, 2)])
print("20)", *[a for a in range(53, 1_000) if f(a, 48, 3) and not f(a, 48, 1)])
print("21)", *[a for a in range(53, 1_000) if f(a, 48, 4) and not f(a, 48, 2)])