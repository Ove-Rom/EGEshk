from itertools import product, permutations


def f(x, y, z, w):
    return x and (z <= w) and not y


for q, w, e, r, t, y, u in product([0, 1], repeat=7):
    tab = [(q, w, 1, e),
           (r, 1, 0, t),
           (1, 0, y, u)]
    if len(set(tab)) == len(tab):
        for p in permutations("xyzw"):
            if [1, 1, 1] == [f(**dict(zip(p, t))) for t in tab]:
                print(*p)
