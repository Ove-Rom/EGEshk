def z(o, v):
    if o in (9, 16): return 0
    if o == v: return 1
    if o < v: return 0
    return z(o - 2, v) + z(o - 2, v) + z(o // 3, v)

print(z(19, 3))