def z(o, v):
    if o == v: return 1
    if o < v: return 0
    return z(o - 2, v) + z(o // 2, v)

print(z(28, 10) * z(10, 1))