with open("17.txt") as f: data = [int(i) for i in f]

maxN = max(i for i in data if str(i)[-2:] == "50")

ans = []

for i in range(len(data) - 2):
    n1, n2, n3 = data[i:i+3]
    c1 = n1 != n2 != n3 != n1
    c2 = len(str(n1)) == len(str(n2)) == len(str(n3)) == 5
    c3 = sum(data[i:i+3]) <= maxN
    if c1 and c2 and c3:
        ans.append(sum(data[i:i+3]))

print(len(ans), max(ans))