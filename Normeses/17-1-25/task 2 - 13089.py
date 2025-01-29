# print("x y z w u")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 for u in 0, 1:
#                     if not ((z <= w) and (y != x)) <= (u == (y or z)):
#                         print(x, y, z, w, u)

from itertools import product, permutations


def f(x, u, y, z, w):
    return ((z <= w) and (y != x)) <= (u == (y or z))

for i in product([0, 1], repeat = 8):
    table = [(0, i[0], 0, 0, 0),
             (0, i[1], i[2], 0, 0),
             (i[3], 0, 0, 0, i[4]),
             (0, 0, i[5], i[6], i[7])]
    if len(set(table)) == len(table):
        for p in permutations("xyzwu"):
            u = not any([f(**dict(zip(p, t))) for t in table])
            if u: print(*p)