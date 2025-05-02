from math import dist

with open("27_B_21720.txt") as f:
    data = [list(map(float, i.split())) for i in f]

def c(cl):
    ans = []
    for d1 in cl:
        s = 0
        for d2 in cl:
            s += dist(d1, d2)
        ans.append([s, d1])
    return min(ans)[1]

eps = 2

cls = []

while data:
    cl = [data.pop()]
    for d1 in cl:
        for d2 in data.copy():
            if dist(d1, d2) < eps:
                cl.append(d2)
                data.remove(d2)
    cls.append(cl)

print([len(i) for i in cls])

cent = [c(i) for i in cls]

px = int(abs(sum(i[0] for i in cent) * 10_000) / len(cent))
py = int(abs(sum(i[1] for i in cent) * 10_000) / len(cent))

print(px, py)