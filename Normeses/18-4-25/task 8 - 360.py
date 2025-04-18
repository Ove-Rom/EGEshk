from itertools import product, repeat

c = 0

for i in product(sorted("инставк"), repeat=4):
    s = "".join(i)
    c1 = i[0] in "нствк"
    c2 = i[-1] in "иа"
    if c1 and c2:
        c += 1
        if s == "ника":
            print(c)
            break