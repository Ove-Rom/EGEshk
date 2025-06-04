from itertools import product

ans = 0

for n, i in enumerate(product(sorted("компьютер"), repeat=5), start=1):
    if n % 2 == 0: continue
    c1 = i[0] != "ь"
    c2 = i.count("к") == 2
    if c1 and c2:
        ans = n

print(ans)