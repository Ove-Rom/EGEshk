from itertools import product, permutations


def f(x, y, z, w):
    return (y <= x) and not z and w


for q, w, e, r, t, y in product([0, 1], repeat=6):
    tab = [(1, 0, q, w),
           (1, 1, e, r),
           (t, 1, 1, y)]
    if len(tab) == len(set(tab)):
        for p in permutations("xyzw"):
            if [1, 1, 1] == [f(**dict(zip(p, t))) for t in tab]:
                print(*p)
