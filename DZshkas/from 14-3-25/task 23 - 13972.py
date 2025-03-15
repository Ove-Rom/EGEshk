def f(a, b, c = 1):
    if a == b: return 1
    if a > b: return 0
    if c: return f(a + 2, b) + \
        f(a + 5, b) + \
        f(a * 2, b)
    else: return f(a + 2, b) + \
        f(a * 2, b)

print(f(7, 23, 0) * f(23, 35))