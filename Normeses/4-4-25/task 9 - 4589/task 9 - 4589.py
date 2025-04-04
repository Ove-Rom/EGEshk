with open("9_4589.txt") as f:
    d = [list(map(int, i.split())) for i in f]

c = 0

for base in d:
    c1 = max(base) < (sum(base) - max(base))
    c2 = max(base) + min(base) == sum(base) - (max(base) + min(base))
    if c1 and c2:
        c += 1

print(c)
