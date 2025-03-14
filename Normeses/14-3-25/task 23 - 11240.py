def f(a, b, c=1):
    if a == b: return 1
    if a > b: return 0
    if c: return f(a + 2, b) + f(a ** 2, 0) + f(a * 3, b)
    return f(a + 2, b) + f(a * 3, b)


print(f(2, 64))
