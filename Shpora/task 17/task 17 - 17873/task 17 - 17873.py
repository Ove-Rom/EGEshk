with open("17_17873.txt") as f:
    data = [int(i) for i in f]

ans = []
minN = min(data)

for n1, n2 in zip(data, data[1:]):
    if any(i % 16 == minN for i in [n1, n2]):
        ans.append(n1 + n2)

print(len(ans), max(ans))