from itertools import product, permutations


def f(x, y, z, w):
    return ((not x) <= y) and ((not y) == z) and w


for q, w, e, r, t, y, u, i in product([0, 1], repeat=8):
    tab = [(0, q, 0, w),
           (0, e, r, t),
           (y, 0, u, i)]
    if len(set(tab)) == len(tab):
        for p in permutations("xyzw"):
            u = all(f(**dict(zip(p, t))) for t in tab)
            if u: print(*p)