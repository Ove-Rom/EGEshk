from itertools import product, permutations


def f(x, y, z, w):
    return not (w <= z) or (x <= y) or (not x)

for i in product([0,1], repeat = 7):
    table = [(1, i[0], i[1], i[2]), (0, 1, 0, i[3]), (i[4], 0, i[5], i[6])]
    if len(set(table)) == len(table):
        for p in permutations("xyzw"):
            u = [f(**dict(zip(p, t))) for t in table] == [0, 0, 0]
            if u: print(*p)