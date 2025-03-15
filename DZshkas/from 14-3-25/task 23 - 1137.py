def f(a, b):
    if a == b: return 1
    if int(a, 2) > int(b, 2): return 0
    return f(bin(int(a, 2) + 1)[2:], b) + \
        f(a + '0', b) + \
        f(a + '1', b)

print(f("100", "11101"))
