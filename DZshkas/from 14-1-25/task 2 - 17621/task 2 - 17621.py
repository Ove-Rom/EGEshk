print("x y z w")

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = not(x <= z) or y == w or y
                if not F: print(x, y, z, w)

# from itertools import product, permutations
#
#
# def f(x, y, z, w):
#     return not(x <= z) or y == w or y
#
#
# for i in product([0, 1], repeat=7):
#     table = [(1, 0, i[0], i[1]),
#              (i[2], 1, 0, i[3]),
#              (0, i[4], i[5], i[6])]
#     if len(table) == len(set(table)):
#         for p in permutations("xyzw"):
#             u = not any(f(**dict(zip(p, t))) for t in table)
#             if u: print(*p)