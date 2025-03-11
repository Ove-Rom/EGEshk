def f(l, r):
    if l == r: return 1
    if l > r: return 0
    return f(l + 1, r) + f(l + 2, r) + f(l + 3, r)

print(f(5, 7) * f(7, 11))