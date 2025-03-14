def f(a, b, flag = 1):
    if a == b and not flag: return 1
    if a > b: return 0
    if a % 2:
        if flag: flag = 0
        else: return 0
    return f(a + 1, b, flag) + f(a + 2, b, flag) + f(a * 2, b, flag)

print(f(2, 40))