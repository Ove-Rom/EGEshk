from math import dist

with open("27_A_21911.txt") as a:
    dataA = [list(map(float, i.split())) for i in a]

with open("27_B_21911.txt") as b:
    dataB = [list(map(float, i.split())) for i in b]

def c(cl):
    ans = []
    for d1 in cl:
        s = 0
        for d2 in cl:
            s += dist(d1, d2)
        ans.append([s, d1])
    return min(ans)[1]

epsA = 2
epsB = 4

clustersA = []
clustersB = []

while dataA:
    cluster = [dataA.pop()]
    for dot in cluster:
        for dot2 in dataA.copy():
            if dist(dot, dot2) < epsA:
                cluster.append(dot2)
                dataA.remove(dot2)
    clustersA.append(cluster)

while dataB:
    cluster = [dataB.pop()]
    for dot in cluster:
        for dot2 in dataB.copy():
            if dist(dot, dot2) < epsB:
                cluster.append(dot2)
                dataB.remove(dot2)
    clustersB.append(cluster)

ca1 = c(clustersA[0])
ca2 = c(clustersA[1])

cb1 = c(clustersB[0])
cb2 = c(clustersB[1])
cb3 = c(clustersB[2])

pxa = int((ca1[0] + ca2[0]) * 10_000 / 2)
pya = int((ca1[1] + ca2[1]) * 10_000 / 2)

pxb = int((cb1[0] + cb2[0] + cb3[0]) * 10_000 / 3)
pyb = int((cb1[1] + cb2[1] + cb3[1]) * 10_000 / 3)

print(pxa, pya)
print(pxb, pyb)