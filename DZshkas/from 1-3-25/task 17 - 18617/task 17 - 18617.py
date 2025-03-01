with open("task 17 - 18617") as f:
    data = [int(i) for i in f]

maxN = max(data) % 3
minN = min(data) % 7

ans = []

for n1, n2 in zip(data, data[1:]):
    c1 = n1 % 3 == maxN or n2 % 3 == maxN
    c2 = n1 % 7 == minN or n2 % 7 == minN

    if c1 and c2:
        ans.append(n1 + n2)

print(len(ans), max(ans))
