data = [list(map(int, i.split())) for i in open("9.txt")]

c = 0

for line in data:
    pov = [line.count(i) for i in line]
    c1 = pov.count(3) == 6# and pov.count(1) == 1
    maxN = max(i for i in line if line.count(i) != 1)
    np = [i for i in line if line.count(i) == 1][0]
    c2 = maxN > np
    if c1 and c2: c+= 1

print(c)