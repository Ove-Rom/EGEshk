from itertools import product, repeat, permutations


def f(x, y, z, w):
    return ((x <= z) <= y) or (not w)

for i in product([0, 1], repeat = 7):
    table = [(1, 0, i[0], i[1]),
             (i[2], 1, 0, i[3]),
             (0, i[4], i[5], i[6])]
    for p in permutations("xyzw"):
        u = [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]
        if u: print(*p)