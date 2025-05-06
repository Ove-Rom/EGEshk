from math import dist

with open("27.17.B_19566.txt") as f:
    data = [list(map(float, i.split())) for i in f]

def c(cl):
    ans = []
    for d1 in cl:
        s = 0
        for d2 in cl:
            s += dist(d1, d2)
        ans.append([s, d1])
    return max(ans)[1]

eps = 2

clast = []

while data:
    cl = [data.pop()]
    for d1 in cl:
        for d2 in data.copy():
            if dist(d1, d2) < eps:
                cl.append(d2)
                data.remove(d2)
    if len(cl) > 10:
        clast.append(cl)

cent = [c(i) for i in clast]

px = int(sum(i[0] for i in cent) * 10_000 / len(cent))
py = int(sum(i[1] for i in cent) * 10_000 / len(cent))

print(px, py)