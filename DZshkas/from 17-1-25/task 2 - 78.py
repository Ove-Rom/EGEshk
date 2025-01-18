from itertools import product, permutations

def f(x,y,z,w):
    return (x <= (y and not z)) or w

for q, w, e, r, t, y, in product([0, 1], repeat=6):
    tab = [(q, w, 1, 0),
           (0, e, r, 1),
           (1, t, 1, y)]
    if len(tab) == len(set(tab)):
        for p in permutations("xyzw"):
            u = not any([f(**dict(zip(p, t))) for t in tab])
            if u: print(*p)