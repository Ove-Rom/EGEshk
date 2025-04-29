with open("27_A_21425.txt") as f:
    cl1a = []
    cl2a = []
    for i in f:
        x, y = map(float, i.split())
        if y < 0:
            cl1a.append([x, y])
        else:
            cl2a.append([x, y])

with open("27_B_21425.txt") as f:
    cl1b = []
    cl2b = []
    cl3b = []
    for i in f:
        x, y = map(float, i.split())
        if y < 0:
            cl1b.append([x, y])
        elif x > 0 < y:
            cl2b.append([x, y])
        else:
            cl3b.append([x, y])


def l(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5

def cent(cl):
    dist = []
    for dot in cl:
        s = 0
        for dot2 in cl:
            s += l(dot[0], dot[1], dot2[0], dot2[1])
        dist.append([s, dot])
    return min(dist)[1]

c1a = cent(cl1a)
c2a = cent(cl2a)

c1b = cent(cl1b)
c2b = cent(cl2b)
c3b = cent(cl3b)

pxa = (c1a[0] + c2a[0]) * 10_000 // 2
pya = (c1a[1] + c2a[1]) * 10_000 // 2

pxb = (c1b[0] + c2b[0] + c3b[0]) * 10_000 // 3
pyb = (c1b[1] + c2b[1] + c3b[1]) * 10_000 // 3

print(pxa, pya)
print(pxb, pyb)