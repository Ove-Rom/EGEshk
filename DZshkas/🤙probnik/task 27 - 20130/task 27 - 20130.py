from itertools import combinations

with open("27A_20130.txt") as a:
    dataA = [list(map(float, i.replace(",", ".").split())) for i in a]

with open("27B_20130.txt") as b:
    dataB = [list(map(float, i.replace(",", ".").split())) for i in b]


def l(x1, x2, y1, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5


cA1 = []
cA2 = []

cB1 = []
cB2 = []
cB3 = []

for x, y in dataA:
    if -2 <= x <= 1:
        cA1.append([x, y])
    else:
        cA2.append([x, y])

for x, y in dataB:
    if -3 <= y <= 2:
        cB1.append([x, y])
    elif 6 <= x <= 10:
        cB2.append([x, y])
    else:
        cB3.append([x, y])

# from turtle import *
#
# tracer(0)
# m = 30
# for x, y in cB1:
#     teleport(x * m, y * m)
#     dot(3, "red")
# for x, y in cB2:
#     teleport(x * m, y * m)
#     dot(3, "green")
# for x, y in cB3:
#     teleport(x * m, y * m)
#     dot(3, "blue")
#
# done()

dA1 = max(combinations(cA1, 2), key=lambda x: l(x[0][0], x[1][0], x[0][1], x[1][1]))
dA2 = max(combinations(cA2, 2), key=lambda x: l(x[0][0], x[1][0], x[0][1], x[1][1]))

dB1 = max(combinations(cB1, 2), key=lambda x: l(x[0][0], x[1][0], x[0][1], x[1][1]))
dB2 = max(combinations(cB2, 2), key=lambda x: l(x[0][0], x[1][0], x[0][1], x[1][1]))
dB3 = max(combinations(cB3, 2), key=lambda x: l(x[0][0], x[1][0], x[0][1], x[1][1]))

pxA = (dA1[0][0] + dA1[1][0] +
       dA2[0][0] + dA2[1][0]) * 10_000 // 4
pyA = (dA1[0][1] + dA1[1][1] +
       dA2[0][1] + dA2[1][1]) * 10_000 // 4

pxB = (dB1[0][0] + dB1[1][0] +
       dB2[0][0] + dB2[1][0] +
       dB3[0][0] + dB3[1][0]) * 10_000 // 6
pyB = (dB1[0][1] + dB1[1][1] +
       dB2[0][1] + dB2[1][1] +
       dB3[0][1] + dB3[1][1]) * 10_000 // 6

print(pxA, pyA)
print(pxB, pyB)
