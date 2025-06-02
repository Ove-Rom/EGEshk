from itertools import product, permutations


def f(x, y ,z, w):
    return not(x <= z) or (y == w) or y

for q,w,e,r,t,y,u in product([1,0], repeat = 7):
    tab = [(1,0,q,w),
           (e,1,0,r),
           (0,t,y,u)]
    if len(set(tab)) == len(tab):
        for p in permutations("xyzw"):
            if [0,0,0] == [f(**dict(zip(p, t))) for t in tab]:
                print(*p)