with open("17_17636.txt") as f:
    data = [int(i) for i in f]

pattern = range(103, 994, 10)

maxN = max(i for i in data if abs(i) in pattern)
ans = []

for n1, n2, n3 in zip(data, data[1:], data[2:]):
    c1 = any(abs(i) in pattern for i in (n1, n2, n3))
    c2 = n1 + n2 + n3 < maxN
    if c1 and c2:
        ans.append(n1 + n2 + n3)

print(len(ans), max(ans))
