def f(p, m):
    if p >= 82: return m % 2 == 1
    if m == 0: return 0
    h = [f(p + 10, m - 1), f(p * 2, m - 1)]
    return all(h) if m % 2 == 0 else any(h)


print("19)", *[p for p in range(1, 82) if f(p, 3)])
print("20)", *[p for p in range(1, 82) if f(p, 4) and not f(p, 2)])
print("21)", *[p for p in range(1, 82) if f(p, 5) and not f(p, 2)])