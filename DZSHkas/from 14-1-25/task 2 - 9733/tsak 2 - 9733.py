# print("x y z w")
#
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 F = (x and not y) or (x == z) or w
#                 if not F: print(x, y, z, w)

from itertools import product, permutations


def f(x, y, z, w):
    return (x and not y) or (x == z) or w


for i in product([0, 1], repeat=4):
    table = [(i[0], i[1], 0, 1),
             (1, 0, i[2], 1),
             (1, 1, 0, i[3])]
    if len(table) == len(set(table)):
        for p in permutations("xyzw"):
            u = not any(f(**dict(zip(p, t))) for t in table)
            if u: print(*p)