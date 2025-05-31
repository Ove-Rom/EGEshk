with open("26_6641.txt") as f:
    n, m = map(int, f.readline().split())
    data = sorted(([int(i.split()[0]), ord(i.split()[1])] for i in f))

count = 0
prS = []
prW = []

for p, t in data.copy():
    if m >= p:
        m -= p
        data.remove([p, t])
        match t:
            case 83: prS.append(p)
            case 87: prW.append(p)

for p, t in data:
    if t == 83 and m + prW[-1] - p >= 0:
        m += prW[-1] - p
        prS.append(p)
        prW.pop()

print(len(prS), m)
