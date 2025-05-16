from math import dist

with open("27_B_18884.txt") as f:
    data = [list(map(float, i.split())) for i in f]

def c(cl):
    ans = []
    for d1 in cl:
        s = 0
        for d2 in cl:
            s += dist(d1, d2)
        ans.append([s, d1])
    return min(ans)[1]

eps = 100
clast = []

while data:
    cl = [data.pop()]
    for d1 in cl:
        for d2 in data.copy():
            if dist(d1, d2) < eps:
                cl.append(d2)
                data.remove(d2)
    clast.append(cl)

cent = [c(i) for i in clast]
print(cent)

sx = int(abs(sum(i[0] for i in cent)) / len(cent))
sy = int(abs(sum(i[1] for i in cent)) / len(cent))

print(sx, sy)