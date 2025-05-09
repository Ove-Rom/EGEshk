def f(a, b, c = None):
    if a == b:
        if c == "c": return 0
        return 1
    if a > b: return 0
    return f(a + 2, b, "a") + f(a + 5, b, "b") + f(a ** 2, b, "c")

print(f(4, 36))