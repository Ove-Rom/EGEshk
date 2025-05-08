from itertools import product, permutations


def f(x, y, z, w):
    return (w == (z <= x)) and y


# 1

print("# 1\n")

for q, w, e, r, t in product([1, 0], repeat=5):
    tab = [(q, 0, w, 0),
           (1, e, 1, 1),
           (r, t, 0, 0)]
    if len(tab) == len(set(tab)):
        for p in permutations("xyzw"):
            if [1, 0, 1] == [f(**dict(zip(p, t))) for t in tab]:
                print(*p)

# 2

print("\n# 2\n")

print("x y z w | res")

for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                print(x, y, z, w, "|", bool(f(x, y, z, w)))

