with open("17_17558.txt") as f:
    data = [int(i) for i in f]

ans = []
count = sum(i % 32 == 0 for i in data)

for n1, n2 in zip(data, data[1:]):
    c1 = any(i < 0 for i in [n1, n2])
    c2 = (n1 + n2) < count
    if c1 and c2:
        ans.append(n1 + n2)

print(len(ans), max(ans))