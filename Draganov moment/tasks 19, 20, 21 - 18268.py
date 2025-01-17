def f(p, q, m):
    if p + q <= 72: return m % 2 == 0
    if m == 0: return 0
    h = [f(p - 3, q, m - 1), f(p, q - 3, m - 1),
         f((p + 1) // 2, q, m - 1), f(p, (q + 1) // 2, m - 1)]
    return all(h) if m % 2 == 0 else any(h)

def f1(p, q, m):
    if p + q <= 72: return m % 2 == 0
    if m == 0: return 0
    h = [f1(p - 3, q, m - 1), f1(p, q - 3, m - 1),
         f1((p + 1) // 2, q, m - 1), f1(p, (q + 1) // 2, m - 1)]
    return any(h) if m % 2 == 0 else any(h)


print("19)", *[p for p in range(23, 460) if f1(50, p, 3)])
print("20)", *[p for p in range(23, 460) if f(50, p, 3) and not f(50, p, 1)])
print("21)", *[p for p in range(23, 460) if f(50, p, 4) and not f(50, p, 2)])