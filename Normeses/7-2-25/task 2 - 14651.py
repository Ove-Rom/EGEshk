from itertools import permutations, product


def f(x, y, z, w):
    return (z <= x) == ((w <= y) or (x and w))


for q, w, e, r, t, y in product([0, 1], repeat=6):
    tab = [(q, w, e, 1),
           (r, t, 1, 1),
           (y, 1, 1, 1)]
    if len(tab) == len(set(tab)):
        for p in permutations("xyzw"):
            u = all(not f(**dict(zip(p, t))) for t in tab)
            if u: print(*p)
