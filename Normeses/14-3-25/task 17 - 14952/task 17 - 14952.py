with open("17_14952.txt") as f:
    data = [int(i) for i in f]

maxN = max([i for i in data if str(i)[-3:] == "121"])

ans = []

for n1, n2, n3 in zip(data, data[1:], data[2:]):
    c1 = len(str(abs(n1))) == 4 and n1 % 2 == 0
    c2 = len(str(abs(n2))) == 4 and n2 % 2 == 0
    c3 = len(str(abs(n3))) == 4 and n3 % 2 == 0
    C1 = c1 + c2 + c3 <= 1
    C2 = n1 + n2 + n3 <= maxN
    if C1 and C2:
        ans.append(n1 + n2 + n3)

print(len(ans), max(ans))
