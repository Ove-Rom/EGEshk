with open("17_2399.txt") as f:
    data = [int(i) for i in f]

sumN = sum(sum(int(j) for j in str(i)) for i in data if i % 35 == 0)

ans = []

for n1, n2 in zip(data, data[1:]):
    c1 = (n1 > sumN) and (hex(n2)[-2:] == "ef" and n2 < sumN)
    c2 = (n2 > sumN) and (hex(n1)[-2:] == "ef" and n1 < sumN)
    if c1 ^ c2:
        ans.append(n1 + n2)

print(len(ans), min(ans))
