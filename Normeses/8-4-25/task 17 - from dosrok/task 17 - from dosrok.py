with open("17.txt") as f:
    data = [int(i) for i in f]

s = sum(i for i in data if i < 0)
ans = []

for i, j, k in zip(data, data[1:], data[2:]):
    line = [i, j, k]
    if min(line) * max(line) > s:
        ans.append(sum(line))

print(len(ans), abs(max(ans)))
