def f(a, b, n):
    if (a + b) >= 77: return n % 2 == 0
    if n == 0: return 0
    h = [f(a + 3, b, n - 1), f(a, b + 3, n - 1),
         f(a * 3, b, n - 1), f(a, b * 3, n - 1)]
    return all(h) if n % 2 == 0 else any(h)

print("19)", *[a for a in range(1, 65) if f(a, 12, 2)])
print("20)", *[a for a in range(1, 65) if f(a, 12, 3) and not f(a, 12, 1)])
print("21)", len([a for a in range(1, 65) if f(a, 12, 4) and not f(a, 12, 2)]))