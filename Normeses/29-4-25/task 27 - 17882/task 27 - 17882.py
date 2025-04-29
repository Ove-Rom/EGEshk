with open("27_A_17882.txt") as f:
    dataa = [list(map(float, i.replace(",", ".").split())) for i in f]


def l(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5


cl1a = []
cl2a = []

for x, y in dataa:
    if x < 1:
        cl1a.append([x, y])
    else:
        cl2a.append([x, y])

c1a = []
c2a = []

for x1, y1 in cl1a:
    s = 0
    for x2, y2 in cl1a:
        s += l(x1, y1, x2, y2)
    c1a.append([s, [x1, y1]])

for x1, y1 in cl2a:
    s = 0
    for x2, y2 in cl2a:
        s += l(x1, y1, x2, y2)
    c2a.append([s, [x1, y1]])


cords1a = min(c1a)[1]
cords2a = min(c2a)[1]

pxa = (cords1a[0] + cords2a[0]) * 10_000 // 2
pya = (cords1a[0] + cords2a[0]) * 10_000 // 2


with open("27_B_17882.txt") as f:
    datab = [list(map(float, i.replace(",", ".").split())) for i in f]


cl1b = []
cl2b = []
cl3b = []

for x, y in datab:
    if x < 3 and y < 4:
        cl1b.append([x, y])
    elif 2 < x < 5 < y:
        cl2b.append([x, y])
    else:
        cl3b.append([x, y])

c1b = []
c2b = []
c3b = []

for x1, y1 in cl1b:
    s = 0
    for x2, y2 in cl1b:
        s += l(x1, y1, x2, y2)
    c1b.append([s, [x1, y1]])

for x1, y1 in cl2b:
    s = 0
    for x2, y2 in cl2b:
        s += l(x1, y1, x2, y2)
    c2b.append([s, [x1, y1]])

for x1, y1 in cl3b:
    s = 0
    for x2, y2 in cl3b:
        s += l(x1, y1, x2, y2)
    c3b.append([s, [x1, y1]])


from turtle import *
m = 10
tracer(0)
for x, y in cl1b:
    teleport(x*m, y*m)
    dot(3, "green")
for x, y in cl2b:
    teleport(x*m, y*m)
    dot(3, "blue")
for x, y in cl3b:
    teleport(x*m, y*m)
    dot(3, "red")
done()






cords1b = min(c1b)[1]
cords2b = min(c2b)[1]
cords3b = min(c3b)[1]

pxb = (cords1b[0] + cords2b[0] + cords3b[0]) * 10_000 // 3
pyb = (cords1b[0] + cords2b[0] + cords3b[0]) * 10_000 // 3

print(pxa, pya)
print(pxb, pyb)
