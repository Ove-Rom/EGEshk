with open("17_12735.txt") as f:
    data = [int(i) for i in f]

maxN = max(i for i in data if str(i)[-2:] == '09')

ans = []

for i, j, k in zip(data, data[1:], data[2:]):
    c1 = sum(l % 7 == 0 for l in (i, j, k)) == 2
    c2 = sum((i, j, k)) < maxN
    if c1 and c2: ans.append(i * j * k)

print(len(ans), min(ans))