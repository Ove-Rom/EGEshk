with open("26_1232.txt") as f:
    s, n = map(int, f.readline().split())
    data = sorted(int(i) for i in f)

count = 0

for c, n in zip(data, data[1:]):
    if s - c - n >= 0:
        s -= c
        count += 1
    elif s - n >= 0: continue
    elif s - n < 0:
        print(count + 1, c)
        break
