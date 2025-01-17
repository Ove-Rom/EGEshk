from itertools import product, permutations


def f(x, y, z, w):
    return not(x == (not z and w)) and (y == (not w and x))

for q, w, e, r, t, y in product([0, 1], repeat = 6):
    table = [(q, w, 0, e),
             (r, 0, t, 0),
             (0, y, 1, 0)]
    if len(set(table)) == len(table):
        for p in permutations("xyzw"):
            u = all([f(**dict(zip(p, t))) for t in table])
            if u: print(*p)