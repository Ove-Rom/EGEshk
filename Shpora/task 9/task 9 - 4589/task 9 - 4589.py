with open("task 9 - 4589.txt") as f:
    data = [list(map(int, i.split())) for i in f]

c = 0

for line in data:
    maxN = max(line)
    c1 = sum(line) - maxN > maxN
    c2 = maxN + min(line) == sum(line) - maxN - min(line)
    if c1 and c2:
        c += 1

print(c)