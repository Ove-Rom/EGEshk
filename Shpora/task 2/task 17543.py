from itertools import product, permutations


def f(x, y, z, w):
    return (y <= (not (x <= z))) or w


for q, w, e, r, t, y, u in product([0, 1], repeat=7):
    tab = [(q, 0, w, e),
           (0, 1, u, r),
           (1, t, y, 0)]
    if len(tab) == len(set(tab)):
        for p in permutations("xyzw"):
            if [0,0,0] == [f(**dict(zip(p, t))) for t in tab]:
                print(*p)
