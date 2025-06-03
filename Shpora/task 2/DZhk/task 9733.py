from itertools import product, permutations


def f(x, y ,z ,w):
    return (x and not y) or (x == z) or w

for q,w,e,r in product([0, 1], repeat=4):
    tab = [(q,w,0,1),
           (1,0,e,1),
           (1,1,0,r)]
    if len(tab) == len(set(tab)):
        for p in permutations("xyzw"):
            if [0,0,0] == [f(**dict(zip(p, t))) for t in tab]:
                print(*p)