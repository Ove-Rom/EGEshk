def f(x, y, m):
    if (x + y) >= 77: return m % 2 == 0
    if m == 0: return 0
    h = [f(x + 3, y, m - 1), f(x, y + 3, m - 1),
         f(x * 3, y, m - 1), f(x, y * 3, m - 1)]
    return all(h) if m % 2 == 0 else any(h)

print("19)", *[x for x in range(1, 65) if f(x, 12, 2)])
print("20)", *[x for x in range(1, 65) if f(x, 12, 3) and not f(x, 12, 1)])
print("21)", *[x for x in range(1, 65) if f(x, 12, 4) and not f(x, 12, 2)])