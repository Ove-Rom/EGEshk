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
# for box in product([0, 1], repeat=7):
#     table = [(1, 0, box[0], box[1]),
#              (box[2], 1, 0, box[3]),
#              (0, box[4], box[5], box[6])]
#     if len(table) == len(set(table)):
#         for p in permutations("xyzw"):
#             u = not any(f(**dict(zip(p, t))) for t in table)
#             if u: print(*p)