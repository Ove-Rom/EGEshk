with open("17_6089.txt") as f:
    data = [int(i) for i in f]

maxN = max(i for i in data if str(i)[-1] == "2")
ans = []

for i in data:
    c1 = i % 3 == 0
    c2 = i % 7
    c3 = i % 17
    c4 = maxN % i == 0
    if c1 and c2 and c3 and c4:
        ans.append(i)

print(len(ans), max(ans))