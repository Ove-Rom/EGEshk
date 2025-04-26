from itertools import product, repeat

for n, s in enumerate(product(sorted("победа", reverse=True), repeat=6), start=1):
    if n % 2: continue
    c1 = s[0] == "о"
    c2 = len(s) == len(set(s))
    if c1 and c2:
        print(n)
        break