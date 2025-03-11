def z(o, v):
    if o == 7 or o < v: return 0
    if o == v: return 1
    return z(o - 1, v) + z(o - 3, v) + z(o // 2, v)

print(z(19, 10) * z(10, 3))