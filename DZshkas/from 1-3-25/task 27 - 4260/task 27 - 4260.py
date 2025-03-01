with open("17_14260.txt") as f:
    data = [int(i) for i in f]

minN = min(i for i in data if len(str(i)) == 4 and str(i)[-1] == str(i)[-2] and i > 0)

ans = []

for n1, n2, n3 in zip(data, data[1:], data[2:]):
    c1 = len(str(abs(n1))) == len(str(abs(n2))) == len(str(abs(n3))) == 3
    c2 = n1 + n2 + n3 > minN
    if c1 and c2: ans.append(n1 + n2 + n3)

print(len(ans), max(ans))
