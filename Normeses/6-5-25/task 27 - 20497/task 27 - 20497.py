from math import dist

with open("27.19.B_20497.txt") as f:
    data = [list(map(float, i.split())) for i in f]

print(len(data))

def c(cl):
    ans = []
    for d1 in cl:
        s = 0
        for d2 in cl:
            s += dist(d1, d2)
        ans.append([s, d1])
    return max(ans)[1]

eps = 3

clast = []

while data:
    cl = [data.pop()]
    for d1 in cl:
        for d2 in data.copy():
            if dist(d1,d2) < eps:
                cl.append(d2)
                data.remove(d2)
    if len(cl) > 10:
        clast.append(cl)

l = [len(i) for i in clast]
print(sum(l), l)

# from turtle import *
# m = 50
# tracer(0)
# for cl, col in zip(clast, ["red", "green", "blue"]):
#     for d in cl:
#         teleport(d[0]*m, d[1]*m)
#         dot(3, col)
# done()

cent = [c(i) for i in clast]

px = int(sum(i[0] for i in cent) * 10_000 / len(cent))
py = int(sum(i[1] for i in cent) * 10_000 / len(cent))

print(px, py)