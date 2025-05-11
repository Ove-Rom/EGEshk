from math import dist

with open("27_A_21931.txt") as f:
# with open("27_B_21931.txt") as f:
    data = [list(map(float, i.split())) for i in f]
    # c1 = []
    # c2 = []
    # c3 = []
    # for i in f:
    #     x, y = map(float, i.split())
        # if y < 10: c1.append([x, y])
        # else: c2.append([x, y])
        # if y < 10: c1.append([x, y])
        # elif x < 17: c2.append([x, y])
        # else: c3.append([x, y])

# clast = [c1, c2, c3]

def c(cl):
    ans = []
    for d1 in cl:
        s = 0
        for d2 in cl:
            s += dist(d1, d2)
        ans.append([s, d1])
    return max(ans)[1]

eps = 1
clast = []

while data:
    cl = [data.pop()]
    for d1 in cl:
        for d2 in data.copy():
            if dist(d1, d2) <= eps:
                cl.append(d2)
                data.remove(d2)
    clast.append(cl)

px = int(c(min(clast, key=len))[0] * 10_000)
py = int(c(max(clast, key=len))[1] * 10_000)

print(px, py)