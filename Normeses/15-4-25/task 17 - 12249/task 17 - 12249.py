with open("17_12249.txt") as f:
    data = [int(i) for i in f]

maxN = max(i for i in data if len(str(abs(i))) == 5 and str(i)[-1] == "3")

ans = []

for i in range(len(data) - 2):
    line = data[i:i+3]
    c1 = any(str(j)[-1] == "3" for j in line)
    c2 = sum(line) <= maxN
    if c1 and c2:
        ans.append(sum(line))

print(len(ans), max(ans))