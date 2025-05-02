from math import dist

with open("27B_19747.txt") as f:
    cl1 = []
    cl2 = []
    cl3 = []
    cl4 = []
    cl5 = []
    for i in f:
        x, y = map(float, i.split())
        l = -3/2*x+24.5
        if x < y < 10:
            cl1.append([x, y])
        elif l > y < x:
            cl2.append([x, y])
        elif l < y < 10:
            cl3.append([x, y])
        elif 10 < y < x:
            cl4.append([x, y])
        elif l < y > x:
            cl5.append([x, y])

def c(cl):
    ans = []
    for d1 in cl:
        s = 0
        for d2 in cl:
            s += dist(d1, d2)
        ans.append([s, d1])
    return min(ans)[1]

cents = [c(i) for i in [cl1, cl2, cl3, cl4, cl5]]
px = int(sum(i[0] for i in cents) * 100_000 / 5)
py = int(sum(i[1] for i in cents) * 100_000 / 5)

print(px, py)