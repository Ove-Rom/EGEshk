def f(a, b):
    if a == b: return 1
    if a < b: return 0
    return f(a - 3, b) + f(a // 3, b)

print(f(35, 8) * f(8, 1))