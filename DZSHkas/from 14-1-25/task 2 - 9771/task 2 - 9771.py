# print("x y z w")
#
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 F = (y <= x) and not z and w
#                 if F: print(x, y, z, w)

from itertools import product, permutations


def f(x, y, z, w):
    return (y <= x) and not z and w


for i in product([0, 1], repeat=6):
    table = [(1, 0, i[0], i[1]),
             (1, 1, i[2], i[3]),
             (i[4], 1, 1, i[5])]
    if len(table) == len(set(table)):
        for p in permutations("xyzw"):
            u = all(f(**dict(zip(p, t))) for t in table)
            if u: print(*p)