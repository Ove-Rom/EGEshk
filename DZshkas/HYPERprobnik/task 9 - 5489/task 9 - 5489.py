with open("9_5489.txt") as f:
    data = [list(map(int, i.split())) for i in f]

c = 0

for tab in data:
    s = set(tab)
    ch = set(i for i in tab if i % 2 == 0)
    nch = s - ch
    c1 = len(s) == 5
    c2 = len(ch) > len(nch)
    c3 = sum(ch) < sum(nch)
    if c1 and c2 and c3: c += 1

print(c)