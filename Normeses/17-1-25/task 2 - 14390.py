from itertools import product, permutations


def f(x, y, z, w):
    return (z and not w) or (z == x) or y

for i in product([0, 1], repeat = 4):
    table = [(i[0], i[1], 0, 1),
             (1, 0, i[2], 1),
             (1, 1, 0, i[3])]
    if len(set(table)) == len(table):
        for p in permutations("xyzw"):
            u = not any([f(**dict(zip(p, t))) for t in table])
            if u: print(*p)