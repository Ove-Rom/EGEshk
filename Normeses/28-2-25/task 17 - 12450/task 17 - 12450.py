with open("17_12450.txt") as f:
    data = [int(i) for i in f]

minN = min(i for i in data if i % 52 == 0)

ans = []

for n1, n2, n3 in zip(data, data[1:], data[2:]):
    o1 = n1 % 113
    o2 = n2 % 113
    o3 = n3 % 113
    if o1 + o2 + o3 == minN:
        ans.append(n1+n2+n3)

print(len(ans), max(ans))