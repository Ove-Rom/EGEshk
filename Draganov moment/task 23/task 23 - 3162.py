def f(a, b, flag=1):
    if a == b and not flag: return 1
    if a > b: return 0
    if flag: return f(a + 1, b) + f(a + 2, b) + f(a * 2, b, 0)
    return f(a + 1, b, 0) + f(a + 2, b, 0)


print(f(2, 12))
