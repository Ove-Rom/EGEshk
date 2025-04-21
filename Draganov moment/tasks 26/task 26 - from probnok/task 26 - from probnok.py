with open("26v2.txt") as f:
    n = f.readline()
    data = [list(map(int, i.split())) for i in f]

data.sort(key = lambda x: (x[0], -x[1]))

p = []

for t, c in data:
    if len(p) < t: p.append(c)
    elif min(p) < c: p[p.index(min(p))] = c

print(sum(p), min(p))