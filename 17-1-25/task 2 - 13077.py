from itertools import product, permutations


def f(x, y, z, w):
    return (w == x) and (y <= z)

def q(x, y, z, w):
    return (w <= x) <= (y == z)

for i in product([0, 1], repeat = 4):
    table = [(1, i[0], 1, 1),
             (i[1], 1, 0, 0),
             (i[2], 0, 0, i[3])]
    if len(set(table)) == len(table):
        for p in permutations("xyzw"):
            u = [1, 1, 0] == [f(**dict(zip(p, t))) for t in table]
            u1 = q(**dict(zip(p, table[0]))) == 0
            u2 = q(**dict(zip(p, table[2]))) == 0
            if u and u1 and u2: print(*p)