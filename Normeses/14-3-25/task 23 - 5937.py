def f(a, b, c = 0):
    if a == b:
        if c <= 15: return 1
        return 0
    if a > b: return 0
    if a % 2 == 0: c += 1
    return f(a + 2, b, c) + f( a + 3, b, c) + f(a * 2 + 1, b, c)

print(f(11, 55))