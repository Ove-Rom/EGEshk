from itertools import product, permutations


def f(h, l, w,n):
    return (not (h <= l)) <= ((not (w <= n)) and h)

for q,w,e,r,t,y in product([0,1], repeat = 6):
    tab = [(0,0,0,q),
           (0,0,w,e),
           (0,r,t,y)]
    if len(set(tab)) == len(tab):
        for p in permutations("hlwn"):
            u = [0,0,0] == [f(**dict(zip(p, t))) for t in tab]
            if u: print(*p)