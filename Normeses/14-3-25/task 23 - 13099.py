def f(a, b, c = 1):
    if a == b: return 1
    if a > b+1: return 0
    if c: return f(a - 1, b, 0) + f(a * 2, b) + f(a * 3, b)
    return f(a * 2, b) + f(a * 3, b)

print(f(3, 15))