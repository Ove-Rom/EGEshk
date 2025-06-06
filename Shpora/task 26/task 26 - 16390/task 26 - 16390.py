with open("26_16390.txt") as f:
    s, n = map(int, f.readline().split())
    data = [int(i) for i in f]

data = sorted(data)
count = 0

for l, r in zip(data, data[1:]):
    if s - l - r >= 0:
        s -= l
        count += 1
    elif s - r >= 0:
        continue
    elif s - r < 0:
        s -= l
        count += 1
        break

print(count, l)