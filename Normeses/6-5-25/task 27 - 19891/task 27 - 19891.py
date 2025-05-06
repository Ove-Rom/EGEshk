with open("27.3.B_19891.txt") as f:
    cl1 = []
    cl2 = []
    cl3 = []
    cl4 = []
    for i in f:
        x, y = map(float, i.split())
        if y > -2 and x < 1:
            cl1.append([x, y])
        elif x > 2 > y > -2:
            cl2.append([x, y])
        elif y > 2:
            cl3.append([x, y])
        else:
            cl4.append([x, y])

from turtle import *
m = 40
tracer(0)
for cl, col in zip([cl1, cl2, cl3, cl4], ["red", "green", "blue", "yellow"]):
    for d in cl:
            teleport(d[0]*m, d[1]*m)
            dot(3, col)
done()

def dist(d1, d2):
    x1, y1 = d1
    x2, y2 = d2
    return max(abs(x2 - x1), abs(y2 - y1))

def c(cl):
    ans = []
    for d1 in cl:
        s = 0
        for d2 in cl:
            s += dist(d1, d2)
        ans.append([s, d1])
    return min(ans)[1]

cent = [c(cl1), c(cl2), c(cl3), c(cl4)]

px = int(sum(i[0] for i in cent) * 10_000 / len(cent))
py = int(sum(i[1] for i in cent) * 10_000 / len(cent))

print(px, py)