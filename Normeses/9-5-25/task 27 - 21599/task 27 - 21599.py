from math import dist

with open("27_B_21599.txt") as f:
    data = [list(map(float, i.split())) for i in f]
#     cl1 = []
#     cl2 = []
#     cl3 = []
#     for i in f:
#         x, y = map(float, i.split())
#         if y > x - 10:
#             cl1.append([x, y])
#         elif y > -5:
#             cl2.append([x, y])
#         else:
#             cl3.append([x, y])
# clast = [cl1, cl2, cl3]

def c(cl):
    ans = []
    for d1 in cl:
        s = 0
        for d2 in cl:
            s += dist(d1, d2)
        ans.append([s, d1])
    return min(ans)[1]

eps = 1.5
clast = []

while data:
    cl = [data.pop(0)]
    for d1 in cl:
        for d2 in data.copy():
            if dist(d1, d2) <= eps:
                cl.append(d2)
                data.remove(d2)
    clast.append(cl)

print(len(clast))

from turtle import *
tracer(0)
m = 10
for d, col in zip(clast, ["red", "green", "blue", "pink", "yellow", "black"]):
    for x, y in d:
        teleport(x*m, y*m)
        dot(3, col)
done()

cent = [c(i) for i in clast]

px = int(abs(sum(i[0] for i in cent)) * 10_000 / len(cent))
py = int(abs(sum(i[1] for i in cent)) * 10_000 / len(cent))

print(px, py)

