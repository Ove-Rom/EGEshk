with open("17_9786.txt") as f: data = [int(i) for i in f]

ans = []

maxN = max(i for i in data if i % 100 == 25)

for i in range(len(data) - 2):
    c1 = len(str(data[i])) == 4
    c2 = len(str(data[i + 1])) == 4
    c3 = len(str(data[i + 2])) == 4
    if (c1 + c2 + c3) <= 2 and sum(data[i:i+3]) <= maxN:
        ans.append(sum(data[i:i+3]))

print(len(ans), max(ans))