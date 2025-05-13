from math import dist

# with open("27A_18056.txt") as f:
with open("27B_18056.txt") as f:
    data = [list(map(float, i.split())) for i in f]

def c(cl):
    ans = []
    for d1 in cl:
        s = 0
        for d2 in cl:
            s += dist(d1, d2)
        ans.append([s, d1])
    return min(ans)[1]

eps = .25
clast = []

while data:
    cl = [data.pop()]
    for d1 in cl:
        for d2 in data.copy():
            if dist(d1, d2) <= eps:
                cl.append(d2)
                data.remove(d2)
    if len(cl) > 20: clast.append(cl)

from turtle import *
tracer(0)
m = 20
for cl, color in zip(clast, ["red", "green", "blue"]):
    for x, y in cl:
        teleport(x*m, y*m)
        dot(3, color)
done()

cent = [c(i) for i in clast]

px = int(abs(sum(i[0] for i in cent)) * 100_000 / len(cent))
py = int(abs(sum(i[1] for i in cent)) * 100_000 / len(cent))

print(px, py)