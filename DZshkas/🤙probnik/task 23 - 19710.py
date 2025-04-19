def f(a, b):
    if a == b: return 1
    if a > b or a == 8: return 0
    return f(a + 3, b) + f(a * 2, b)

print(f(2, 32) * f(32, 76))