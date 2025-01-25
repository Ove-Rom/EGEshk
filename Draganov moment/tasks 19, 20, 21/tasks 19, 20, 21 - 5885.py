def f(p, m):
    if p == 42: return m % 2 == 1
    if m == 0: return 0
    if p < 42:
        h = [f(p + 1, m - 1), f(p + 3, m - 1), f(p + 7, m - 1)]
    else:
        h = [f(p - 1, m - 1), f(p - 3, m - 1), f(p - 7, m - 1)]
    return all(h) if (m+1) % 2 == 0 else any(h)

def f1(p, m):
    if p == 42: return m % 2 == 1
    if m == 0: return 0
    if p < 42:
        h = [f(p + 1, m - 1), f(p + 3, m - 1), f(p + 7, m - 1)]
    else:
        h = [f(p - 1, m - 1), f(p - 3, m - 1), f(p - 7, m - 1)]
    return any(h) if (m+1) % 2 == 0 else any(h)


print("19)", *[p for p in range(0, 100) if f1(p, 3)])
print("20)", *[p for p in range(0, 100) if f(p, 4) and not f(p, 1)])
print("21)", *[p for p in range(0, 100) if f(p, 5) and not f(p, 2)])