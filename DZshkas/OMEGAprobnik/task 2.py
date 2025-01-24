from itertools import product, permutations


def f(x, y, z, w):
    return (w and y) or ((x <= w) == (y <= z))


for q, w, e, r, t, y in product([0, 1], repeat=6):
    tab = [(q, w, e, 1),
           (1, r, t, 1),
           (1, y, 1, 1)]
    if len(set(tab)) == len(tab):
        for p in permutations("xyzw"):
            u = not any(f(**dict(zip(p, t))) for t in tab)
            if u:
                print(*p)

# print("x y z w")
# for x in 0,1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (w and y) or (x <= (w == y) <= z)
#                 if not f:
#                     print(x, y, z, w)
