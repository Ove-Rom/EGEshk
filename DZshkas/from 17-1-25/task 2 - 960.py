from itertools import permutations


def f(a, b, c):
    return a and not b or c


tab = [(0, 0, 0),
       (0, 0, 1),
       (0, 1, 0),
       (0, 1, 1),
       (1, 0, 0),
       (1, 0, 1),
       (1, 1, 0),
       (1, 1, 1)]
for p in permutations("abc"):
    u = [0, 1, 1, 1, 0, 0, 1, 1] == [f(**dict(zip(p, t))) for t in tab]
    if u: print(*p)
