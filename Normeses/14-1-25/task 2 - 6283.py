from itertools import product, permutations


def f(x, y, z, w):
    return not(not(x <= (not w)) and z) and (not (w <= z)) and (x <= (not z))

count = []

for i in product([0, 1], repeat = 5):
    table = [(1, 0, i[0], 0),
             (1, 0, i[1], i[2]),
             (i[3], 1, i[4], 1)]
    for p in permutations("xyzw"):
        u = [f(**(dict(zip(p, t)))) for t in table] == [1, 0, 0]
        if u: count.append(p)

print(len(set(count)))