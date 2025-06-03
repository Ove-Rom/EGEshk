with open("task 9 - 17550.txt") as f:
    data = [list(map(int, i.split())) for i in f]

count = 0

for line in data:
    pov = [line.count(i) for i in line]
    c1 = pov.count(3) == 3 == pov.count(1)
    p = [i for i in line if line.count(i) != 1]
    np = [i for i in line if line.count(i) == 1]
    c2 = sum(p) ** 2 > sum(np) ** 2
    if c1 and c2:
        count += 1

print(count)