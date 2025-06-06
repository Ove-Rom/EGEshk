with open("26_12256.txt") as f:
    s, n = map(int, f.readline().split())
    data = sorted(int(i) for i in f)

count = 0

for l, r in zip(data, data[1:]):
    if s - l - r >= 0:
        s -= l
        count += 1
    elif s - r >= 0: continue
    elif s - r < 0:
        count += 1
        s -= l
        break

print(count, l)
