with open("27A_18050.txt") as f:
    f.readline()
    k1a = []
    k2a = []
    for star in f:
        x, y = map(float, star.replace(",", ".").split())
        if x < 0.55 and y < 3.5:
            k1a.append([x, y])
        else:
            k2a.append([x, y])


def length(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5


center1 = min(k1a, key=lambda star: \
    sum(length(star[0], star[1], x, y) for x, y in k1a))

center2 = min(k2a, key=lambda star: \
    sum(length(star[0], star[1], x, y) for x, y in k2a))

ansAx = (center1[0] + center2[0]) * 10_000 // 2
ansAy = (center1[1] + center2[1]) * 10_000 // 2

with open("27B_18050.txt") as f:
    f.readline()
    k1b = []
    k2b = []
    k3b = []
    for star in f:
        x, y = map(float, star.replace(",", ".").split())
        f1 = 5 * x / 3
        f2 = 14 - x
        if f1 < y < f2:
            k1b.append([x, y])
        elif f2 < y < f1:
            k2b.append([x, y])
        elif y < f1 and y < f2:
            k3b.append([x, y])

# from turtle import *
#
# screensize(2000, 2000)
# tracer(0)
#
# for x, y in k1b:
#     teleport(x*100, y*100)
#     dot(3, "blue")
#
# for x, y in k2b:
#     teleport(x*100, y*100)
#     dot(3, "red")
#
# for x, y in k3b:
#     teleport(x*100, y*100)
#     dot(3, "green")
# done()

center1 = min(k1b, key=lambda star: \
    sum(length(star[0], star[1], x, y) for x, y in k1b))
center2 = min(k2b, key=lambda star: \
    sum(length(star[0], star[1], x, y) for x, y in k2b))
center3 = min(k3b, key=lambda star: \
    sum(length(star[0], star[1], x, y) for x, y in k3b))

ansBx = (center1[0] + center2[0] + center3[0]) * 10_000 // 3
ansBy = (center1[1] + center2[1] + center3[1]) * 10_000 // 3

print(ansAx, ansAy)
print(ansBx, ansBy)
