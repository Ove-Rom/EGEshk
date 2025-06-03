from itertools import product, permutations


def f(a, b, c, d):
    return (not a and not b) or (b == c) or d

for q,w,e,r in product([0, 1], repeat=4):
    tab = [(q,w,1,e),
           (1,0,r,1),
           (0,0,1,1)]
    if len(tab) == len(set(tab)):
        for p in permutations("abcd"):
            if [0,0,0] == [f(**dict(zip(p, t))) for t in tab]:
                print(*p)