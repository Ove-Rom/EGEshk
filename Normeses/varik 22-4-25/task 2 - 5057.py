from itertools import product, permutations


def f(x, y, z, w):
    return (w <= (y == z)) and (y == (z <= x))


for q, w in product([1, 0], repeat=2):
    tab = [(q, 0, 0, 0),
           (0, w, 1, 1),
           (0, 0, 0, 1)]
    if len(set(tab)) == len(tab):
        for p in permutations("xyzw"):
            if [1, 1, 0] == [f(**dict(zip(p, t))) for t in tab]:
                print(*p)
