def g(o, l):
    if o == l: return 1
    if o < l: return 0
    return g(o - 1, l) + g(o // 2, l)

print(g(30, 8) * g(8, 1))