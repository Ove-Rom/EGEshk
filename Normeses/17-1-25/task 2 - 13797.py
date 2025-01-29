from itertools import product, permutations


def f (x, y, z, w):
    return (not x and (z <= y) and not w) or ((z == w) and ((x or y) <= w))

for i in product([0, 1], repeat = 4):
    table = [(1 , 0, 0, 0),
             (i[0], 1, 0, i[1]),
             (1, 0, i[2], i[3])]
    if len(set(table)) == len(table):
        for p in permutations("xyzw"):
            u = all([f(**dict(zip(p, t))) for t in table])
            if u: print(*p)