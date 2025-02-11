with open("17_9840.txt") as f: data = [int(i) for i in f]

maxN = max(i for i in data if len(str(abs(i))) == 4 and abs(i) % 100 == 39)

ans = []

for i in range(len(data) - 1):
    n1, n2 = data[i:i+2]

    c1 = len(str(abs(n1))) == 4
    c2 = len(str(abs(n2))) == 4
    if c1 ^ c2 and sum(data[i:i+2])**2 <= maxN**2:
        ans.append(sum(data[i:i+2]))

print(len(ans), max(ans))