with open("task 9 - 9740.txt") as f:
    data = [list(map(int, i.split())) for i in f]

c = 0

for line in data:
    pov = [line.count(i) for i in line]
    c1 = pov.count(3) == 3 and pov.count(1) == 4
    p = [i for i in line if line.count(i) != 1]
    np = [i for i in line if line.count(i) == 1]
    if not c1: continue
    c2 = sum(np) / 4 <= p[0]
    if c2:
        c += 1

print(c)