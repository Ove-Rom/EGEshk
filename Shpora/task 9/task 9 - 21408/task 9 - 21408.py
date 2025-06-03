with open("task 9 - 21408.txt") as f:
    data = [list(map(int, i.split())) for i in f]

count = 0

for line in data:
    pov = [line.count(i) for i in line]
    c1 = pov.count(3) == 6 and pov.count(1) == 1
    if not c1: continue
    p = [i for i in line if line.count(i) != 1]
    np = sum(line) - sum(p)
    c2 = max(p) > np
    if c1 and c2:
        count += 1

print(count)
