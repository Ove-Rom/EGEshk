from itertools import permutations


def f(x,y,z):
    return not(x == (y <= z))

tab = [(0,0,1),
       (0,1,1)]
for p in permutations("xyz"):
    u = [1, 0] == [f(**dict(zip(p, t))) for t in tab]
    if u: print(*p)