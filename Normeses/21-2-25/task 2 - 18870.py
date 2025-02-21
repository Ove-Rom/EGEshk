from itertools import product, permutations


def f(x, y, z, w):
    return ((x <= z) <= w) or not y

for q,w,e,r,t,y,u in product([0, 1], repeat=7):
    tab = [(q,w,1,e),
           (r,0,t,y),
           (u,1,0,0)]
    if len(tab) == len(set(tab)):
        for p in permutations("xyzw"):
            u = [f(**dict(zip(p, t))) for t in tab] == [0,0,0]
            if u: print(*p)