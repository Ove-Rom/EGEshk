with open("17_17873.txt") as f: data = [int(i) for i in f]

minN = min(data)

ans = []

for i in range(len(data) - 1):
    n1, n2 = data[i:i + 2]
    c1 = n1 % 16 == minN
    c2 = n2 % 16 == minN
    if c1 or c2:
        ans.append(n1 + n2)

print(len(ans), max(ans))
