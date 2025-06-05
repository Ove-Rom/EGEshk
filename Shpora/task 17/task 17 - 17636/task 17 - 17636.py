with open("17_17636.txt") as f:
    data = [int(i) for i in f]

maxN = max(i for i in data if str(i)[-1] == "3" and len(str(abs(i))) == 3)
ans = []

for n1, n2, n3 in zip(data, data[1:], data[2:]):
    c1 = any(str(i)[-1] == "3" and len(str(abs(i))) == 3 for i in [n1, n2, n3])
    c2 = sum((n1, n2, n3)) < maxN
    if c1 and c2:
        ans.append(n1 + n2 + n3)

print(len(ans), max(ans))