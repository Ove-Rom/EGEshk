with open("17_4705.txt") as f: data = [int(i) for i in f]

maxN = max(i for i in data if str(i)[-1] == '3')

ans = []

for i in range(len(data) - 1):
    n1, n2 = data[i:i + 2]

    c1 = str(n1)[-1] == '3'
    c2 = str(n2)[-1] == '3'

    if c1 ^ c2 and (n1 ** 2 + n2 ** 2) >= maxN**2:
        ans.append(n1 ** 2 + n2 ** 2)

print(len(ans), max(ans))
