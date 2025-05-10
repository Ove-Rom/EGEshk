def f(a, b):
    if a == b: return 1
    if a < b or a == 15: return 0
    return f(a - 2, b) + f(a - 3, b) + f(a // 3, b)

print(f(48, 25) * f(25, 17) * f(17, 4))