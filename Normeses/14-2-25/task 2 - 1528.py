from itertools import product, permutations


def f(x, y, z, w):
    return not w and ((y or z) <= (y and not x))


for q, w, e, r, t, y, u, i in product([0, 1], repeat=8):
    tab = [(q, w, e, 1),
           (r, t, 1, y),
           (u, 1, 1, i)]
    if len(tab) == len(set(tab)):
        for p in permutations("xyzw"):
            u = all(f(**dict(zip(p, t))) for t in tab)
            if u: print(*p)
