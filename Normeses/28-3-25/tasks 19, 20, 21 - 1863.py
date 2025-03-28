def f(a, n):
    if a >= 40: return n % 2 == 0
    if n == 0: return 0
    h = [f(a + 1, n - 1), f(a + 4, n - 1), f(a * 2, n - 1)]
    return all(h) if n % 2 == 0 else any(h)

print("19)", *[a for a in range(1, 40) if f(a, 2) and not f(a, 1)])
print("20)", *[a for a in range(1, 40) if f(a, 3) and not f(a, 1)])
print("21)", *[a for a in range(1, 40) if f(a, 4) and not f(a, 2)])