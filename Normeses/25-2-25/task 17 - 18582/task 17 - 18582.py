with open("17_18582.txt") as f:
    data = [int(i) for i in f]

minN = str(min(data))[-1]
ans = []

for n1, n2, n3 in zip(data, data[1:], data[2:]):
    c1 = sum((n1 >= 0, n2 >= 0, n3 >= 0)) < sum((n1 < 0, n2 < 0, n3 < 0))
    c2 = str(sum((n1, n2, n3)))[-1] == minN
    if c1 and c2:
        ans.append((abs(sum((n1, n2, n3)))))

print(len(ans), max(ans))