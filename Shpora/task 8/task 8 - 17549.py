from itertools import product

ans = []

for n, i in enumerate(product(sorted("фокус"), repeat=5), start=1):
    s = "".join(i)
    c1 = "ф" not in s
    c2 = s.count("у") == 2
    if c1 and c2:
        ans.append(n)

print(max(ans))