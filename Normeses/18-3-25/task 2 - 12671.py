from itertools import product, permutations


def f(x, y, z, w):
    return not(x == (w and not z)) and (y == (x and not w))

for q,w,e,r,t,y in product([0,1], repeat=6):
    tab = [(q,w,0,e),
           (r,0,t,0),
           (0,y,1,0)]
    if len(tab) == len(set(tab)):
        for p in permutations("xyzw"):
            u = all(f(**dict(zip(p, t))) for t in tab)
            if u: print(*p)