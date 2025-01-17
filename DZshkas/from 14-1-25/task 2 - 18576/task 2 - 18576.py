# print("x y z w")
#
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 F = not(w <=(x == y)) and (z <= x)
#                 if F: print(x, y, z, w)

from itertools import product, permutations


def f(x, y, z, w):
    return not(w <=(x == y)) and (z <= x)


for i in product([0, 1], repeat=5):
    table = [(i[0], 1, 1, i[1]),
             (0, i[2], i[3], 0),
             (i[4], 0, 1, 0)]
    if len(table) == len(set(table)):
        for p in permutations("xyzw"):
            u = all(f(**dict(zip(p, t))) for t in table)
            if u: print(*p)