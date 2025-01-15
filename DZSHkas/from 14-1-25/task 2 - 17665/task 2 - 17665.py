# print("x y z w")
#
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 F = (z <= (not (y <= x))) or w
#                 if not F: print(x, y, z, w)

from itertools import product, permutations


def f(x, y, z, w):
    return (z <= (not (y <= x))) or w


for i in product([0, 1], repeat=7):
    table = [(i[0], 1, i[1], i[2]),
             (i[3], i[4], 0, 0),
             (i[5], 0, 1, i[6])]
    if len(table) == len(set(table)):
        for p in permutations("xyzw"):
            u = not any([f(**dict(zip(p, t))) for t in table])
            if u: print(*p)
