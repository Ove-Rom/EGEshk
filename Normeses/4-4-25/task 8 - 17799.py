from itertools import product

for n, s in enumerate(product(sorted("аргумент"), repeat=4), start=1):
    s = ''.join(s)
    c1 = len(s) == len(set(s))
    c2 = ''.join(sorted(s)) == s
    if c1 and c2:
        print(n)
