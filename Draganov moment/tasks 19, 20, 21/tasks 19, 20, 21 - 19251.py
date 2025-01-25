def f(p, m):
    if p >= 132: return m % 2 == 0
    if m == 0: return 0
    h = [f(p +3 , m - 1), f(p +6, m - 1), f(p * 3, m - 1)]
    return all(h) if m % 2 == 0 else any(h)

print("19)", *[p for p in range(1, 132) if f(p, 2)])
print("20)", *[p for p in range(1, 132) if f(p, 3) and not f(p, 1)])
print("21)", *[p for p in range(1, 132) if f(p, 4) and not f(p, 2)])