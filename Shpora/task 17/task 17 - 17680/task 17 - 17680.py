with open("17_17680.txt") as f:
    data = [int(i) for i in f]

minN = min(i for i in data if i > 0 and i % 41 == 0)
ans = []

for n1, n2 in zip(data, data[1:]):
    c1 = n1 != n2
    c2 = abs(n1 - n2) % minN == 0
    if c1 and c2:
        ans.append(n1 + n2)

print(len(ans), max(ans))