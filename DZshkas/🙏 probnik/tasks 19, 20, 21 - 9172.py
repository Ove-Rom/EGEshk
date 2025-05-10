def f(a, n):
    if a >= 100: return n % 2 == 0
    if n == 0: return 0
    h = [f(a + 7, n - 1), f(a * 2, n - 1)]
    return all(h) if n % 2 == 0 else any(h)

def fp(a, n):
    if a >= 100: return n % 2 == 0
    if n == 0: return 0
    h = [fp(a + 7, n - 1), fp(a * 2, n - 1)]
    return any(h)

print("19)", *[a for a in range(1, 100) if fp(a, 1) and fp(a, 2)])
print("20)", *[a for a in range(1, 100) if not fp(a, 1) and f(a, 2) and fp(a, 3)])
print("21)", *[a for a in range(1, 100) if f(a, 4) and not f(a, 2)])

