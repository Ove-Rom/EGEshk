from itertools import product, repeat, permutations


def f(x, y ,z, w):
    return (z <= w) and y and not x

for q,w,e,r,t in product([1, 0], repeat=5):
    tab = [(0,1,q,0),
           (w,0,e,r),
           (0,1,1,t)]
    if len(set(tab)) == len(tab):
        for p in permutations("xyzw"):
            if [1,1,0] == [f(**dict(zip(p, t))) for t in tab]:
                print(*p)
