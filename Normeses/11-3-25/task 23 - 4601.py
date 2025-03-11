def z(o, v):
    if o == v: return 1
    if o < v: return 0
    return z(o - 1, v) + z(o // 2, v)

print(z(30, 12) * z(12, 1))