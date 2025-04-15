def f(a, b):
    if a == b: return 1
    if a > b or a == 21: return 0
    return f(a + 2, b) + f(a + 3, b) + f(a * 2, b)


print(f(7, 14) * f(14, 32))