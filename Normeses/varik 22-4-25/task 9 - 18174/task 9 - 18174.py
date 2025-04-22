with open("9_18174.txt") as f:
    data = [list(map(int, i.split())) for i in f]

c = 0

for line in data:
    c1 = len(set(line)) == len(line) - 1
    smin = smax = 0
    for i in line:
        if i > 0:
            smax += i
        else: smin += i
    if c1 and abs(smin) > smax:
        c += 1

print(c)