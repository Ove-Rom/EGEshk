from itertools import combinations

with(open("17_7718.txt")) as f:
    data = [int(i) for i in f]

ans = []

for n1, n2 in combinations(data, 2):
    c1 = (n1 + n2) % 18 == 0
    c2 = n1 * n2 % 18 == 0
    if c1 ^ c2:
        ans.append(n1 + n2)

print(len(ans), max(ans))
