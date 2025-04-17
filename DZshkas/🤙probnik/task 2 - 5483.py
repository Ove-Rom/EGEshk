from itertools import product, permutations


def f(x, y, z, w):
    return (z == (not x)) <= ((w <= (not y)) and (y <= x))


for q, w, e, r, t in product([0, 1], repeat=5):
    tab = [(1, 1, 1, 0),
           (q, w, 0, 0),
           (e, 0, r, t)]
    if len(tab) == len(set(tab)):
        for p in permutations("xyzw"):
            if [1, 0, 0] == [f(**dict(zip(p, t))) for t in tab]:
                print(*p)
