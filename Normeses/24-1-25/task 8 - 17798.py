from itertools import product

s = "мнс"
g = "иу"
c = 0

for i in product(sorted("минус"), repeat = 4):
    c += 1
    c1 = sum(i.count(j) for j in s)
    c2 = sum(i.count(j) for j in g)
    if c1 >= c2:
        print(c)
