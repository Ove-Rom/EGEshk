from itertools import product

ans = 0

for n, i in enumerate(product(sorted("победа"), repeat=6), start=1):
    if n % 2: continue
    s = "".join(i)
    c1 = s[0] == "о"
    c2 = len(set(s)) == len(s)
    if c1 and c2:
        ans = n

print(ans)