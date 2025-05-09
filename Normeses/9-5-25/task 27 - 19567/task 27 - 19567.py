from math import dist

with open("27.13.B_19567.txt") as f:
    data = [list(map(float, i.split())) for i in f]
print(len(data))

def c(cl):
    ans = []
    for d1 in cl:
        s = 0
        for d2 in cl:
            s += dist(d1, d2)
        ans.append([s, d1])
    return min(ans)[1]

eps = .4

clast = []

while data:
    cl = [data.pop()]
    for d1 in cl:
        for d2 in data.copy():
            if dist(d1, d2) <= eps:
                cl.append(d2)
                data.remove(d2)
    clast.append(cl)

print(len(clast))

cent = [c(i) for i in clast]

px = int(abs(sum(i[0] for i in cent)) * 10_000 / len(cent))
py = int(abs(sum(i[1] for i in cent)) * 10_000 / len(cent))

print(px, py)