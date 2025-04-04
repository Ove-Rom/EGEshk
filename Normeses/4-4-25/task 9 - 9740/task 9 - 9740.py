d = [tuple(map(int, i.split())) for i in open("9_9740.txt")]

c = 0

for i in d:
    np = {j for j in i if i.count(j) == 1}
    p = set(i) - np
    c1 = len(p) == 1
    c2 = sum(np) / len(np) <= sum(p)
    if c1 and c2:
        c += 1

print(c)
