from itertools import product
ans = []
for n, s in enumerate(product(sorted("marksl"), repeat=6), start=1):
    s = ''.join(s)
    c1 = "ks" not in s and "sk" not in s
    countL = [s.count(i) for i in s]
    c2 = sum(countL) == 12 and 3 in countL
    print(countL)
    if c1 & c2:
        ans.append(n)

print(max(ans))