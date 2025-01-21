def f(a, b, m):
    if a >= 50 or b >= 50:
        if a + b <= 109:
            return m % 2 == 0
        else: return m % 2 != 0
    if m == 0: return 0
    h = [f(a + 1, b, m - 1), f(a, b + 1, m - 1),
         f(a + 2, b, m - 1), f(a, b + 2, m - 1),
         f(a * 2, b, m - 1), f(a, b * 2, m - 1), ]
    return all(h) if m % 2 == 0 else any(h)

print("19)", *[a for a in range(1, 50) if f(a, 24, 3) and not f(a, 24, 1)])
print("20)", *[a for a in range(1, 50) if f(a, 24, 4) and not f(a, 24, 2)])
print("21)", *[a for a in range(1, 50) if f(a, 24, 4) and not f(a, 24, 2)])