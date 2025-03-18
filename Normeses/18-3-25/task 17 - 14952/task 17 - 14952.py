with open("17_14952.txt") as f:
    data = [int(i) for i in f]

maxN = max(i for i in data if str(i)[-3:] == "121")

ans = []

pattern = list(range(1000, 10000, 2))

for n1, n2, n3 in zip(data, data[1:], data[2:]):
    c1 = sum(abs(i) in pattern for i in [n1, n2, n3]) <= 1
    c2 = n1 + n2 + n3 <= maxN
    if  c1 and c2: ans.append(n1 + n2 + n3)


print(len(ans), max(ans))