with open("27_A_17916.txt") as a:
    cla1 = []
    cla2 = []
    for i in a:
        x, y = map(float, i.split())
        if y < 8: cla1.append([x, y])
        else: cla2.append([x, y])

with open("27_B_17916.txt") as b:
    clb1 = []
    clb2 = []
    clb3 = []
    clb4 = []
    clb5 = []
    for i in b:
        x, y = map(float, i.split())
        if x < 7 and y < 5:
            clb1.append([x, y])
        elif 5 < y < 9:
            clb2.append([x, y])
        elif 10 < y < 13:
            clb3.append([x, y])
        elif 14 < y:
            clb4.append([x, y])
        else:
            clb5.append([x, y])

def l(d1, d2):
    x1, y1 = d1
    x2, y2 = d2
    return ((x2 - x1) ** 2 + (y2 - y1)**2)**.5

def c(cl):
    ans = []
    for d1 in cl:
        s = 0
        for d2 in cl:
            s += l(d1, d2)
        ans.append([s, d1])
    return min(ans)[1]

ca1 = c(cla1)
ca2 = c(cla2)

cb1 = c(clb1)
cb2 = c(clb2)
cb3 = c(clb3)
cb4 = c(clb4)
cb5 = c(clb5)

pxa = int((ca1[0] + ca2[0]) * 10_000 / 2)
pya = int((ca1[1] + ca2[1]) * 10_000 / 2)

pxb = int((cb1[0] + cb2[0] + cb3[0] +
           cb4[0] + cb5[0]) * 10_000 / 5)
pyb = int((cb1[1] + cb2[1] + cb3[1] +
           cb4[1] + cb5[1]) * 10_000 / 5)

print([pxa, pya], [pxb, pyb], sep="\n")