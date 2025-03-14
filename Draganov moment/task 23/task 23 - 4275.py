def f(a, b, c):
    if a == b and c <= 3: return 1
    if a > b: return 0
    return f(a + 2, b, c) + f(a * 3, b, c + 1) + f(a * 5, b, c + 1)

print(f(2, 200, 0))