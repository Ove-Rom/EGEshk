from math import dist

with open("27_A_21931.txt") as f:
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

eps = 1
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

cents = [c(i) for i in cls]

print(cents[1][0]*10000, cents[0][1]*10000)