from itertools import product, permutations


def f(a, b, c, d):
    return not (b <= a) and (c <= d) or a and b and c and not d


for q, w, e, r, t, y, u, i, o in product([0, 1], repeat=9):
    tab = [(q, 0, 0, 0),
           (w, e, r, 0),
           (t, y, 0, 0),
           (u, 0, i, o)]
    if len(tab) == len(set(tab)):
        for p in permutations("abcd"):
            u = all([f(**dict(zip(p, t))) for t in tab])
            if u: print(*p)
