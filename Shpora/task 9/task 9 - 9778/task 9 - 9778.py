with open("task 9 - 9778.txt") as f:
    data = [list(map(int, i.split()))for i in f]

for n, line in enumerate(data, start=1):
    pov = [line.count(i) for i in line]
    c1 = pov.count(2) == 2 and pov.count(1) == 4
    p = [i for i in line if line.count(i) != 1]
    if not p: continue
    np = sum(line) - p[0]
    c2 = p[0] >= np/4
    if c1 and c2:
        print(n)
        break