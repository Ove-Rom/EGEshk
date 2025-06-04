from itertools import product

ans = 0

for n, i in enumerate(product(sorted("мангуст"), repeat=6), start=1):
    c1 = i[0] != "у"
    c2 = i.count("м") == 2
    c3 = i.count("г") <= 1
    if c1 and c2 and c3:
        ans = n

print(ans)