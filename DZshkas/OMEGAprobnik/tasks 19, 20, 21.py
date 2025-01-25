def f(a, b, m):
    if (a + b) >= 300: return m % 2 == 0
    if m == 0: return 0
    h = [f(a + 3, b, m - 1), f(a, b + 3, m - 1),
         f(a * 2, b, m - 1), f(a, b * 2, m - 1)]
    return any(h) if (m + 1) % 2 == 0 else all(h)

print("19)", *[a for a in range(1, 280) if f(a, 20, 2)])
print("20)", *[a for a in range(1, 280) if f(a, 20, 3) and not f(a, 20, 1) ])
print("21)", *[a for a in range(1, 280) if f(a, 20, 5) and not f(a, 20, 3) ])