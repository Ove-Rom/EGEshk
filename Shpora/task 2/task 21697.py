from itertools import product, permutations


def f(x, y, z, w):
    return not (x <= y) or (z == w) or z


for q, w, e, r, t, y, u in product([0, 1], repeat=7):
   tab = [(0,0,q,w),
          (e,r,1,t),
          (y,1,0,u)]
   if len(set(tab)) == len(tab):
       for p in permutations("xyzw"):
           if [0,0,0] == [f(**dict(zip(p, t))) for t in tab]:
               print(*p)