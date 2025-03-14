def f(a, b, c):
    if a > b: return 0
    if c == 51:
        if a == b: return 1
        return 0
    return f(a * 4, b, c + 1) + f(a + 1, b, c + 1) + f(a * 3, b, c + 1)

print(f(2, 404, 0))