from itertools import product, permutations
from timeit import repeat


def f(a, b, c, d):
    return ((a <= b) == c) or not d and(d <= (not a))

for i in product([0, 1], repeat = 9):
    table = [(0, i[0], i[1], i[2]),
             (i[3], i[4], 0, i[5]),
             (0, i[6], i[7], 0),
             (0, i[8], 0, 0)]
    if len(set(table)) == len(table):
        for p in permutations("abcd"):
            u = not any([f(**dict(zip( p, t))) for t in table])
            if u: print(*p)