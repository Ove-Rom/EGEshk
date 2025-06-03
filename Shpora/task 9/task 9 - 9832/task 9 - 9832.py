with open("task 9 - 9832.txt") as f:
    data = [list(map(int, i.split())) for i in f]

for line in data:
    pov = [line.count(i) for i in line]
    c1 = pov.count(2) == 4 and pov.count(1) == 3
    c2 = line.count(max(line)) == 1
    if c1 and c2:
        print(sum(line))
        break