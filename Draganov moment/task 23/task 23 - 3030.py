def f(a, b, flag = 1):
    if a == b: return 1
    if a > b: return 0
    if flag: return f(a + 1, b) + f(a + 2, b) + f(a * 2, b, 0)
    return f(a + 1, b, 1) + f(a + 2, b, 1)

print(f(1, 15))