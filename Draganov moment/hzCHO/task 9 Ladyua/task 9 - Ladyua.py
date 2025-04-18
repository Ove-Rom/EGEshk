with open("9v1.txt") as f:
    data = [list(map(int, i.split())) for i in f]

c = 0

for line in data:
    c1 = all(1 <= i <= 8 for i in line)
    c2 = (line[0] == line[2]) ^ (line[1] == line[3])
    if c1 and c2: c += 1

print(c)