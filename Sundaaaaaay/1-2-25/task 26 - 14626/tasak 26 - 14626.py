# with open("test") as f:
with open("26_14626.txt") as f:
    f.readline()
    k, m = map(int, f.readline().split())
    caves = sorted(map(int, f.readline().split()))
    packs = sorted(int(i) for i in f)

data = []

for i in range(len(packs)):
    if i % 2 == 0:
        data.append(packs.pop(-1))
    else:
        data.append((packs.pop(0)))

voidSpace = dict()

minVoidSpace = 99999999
sumVoidSpace = 0

print(m, sum(data), len(caves)*m)

for i in caves:
    caveM = 0
    while caveM + data[0] < m:
        caveM + data.pop(0)
        if not data:
            exit(300)
    voidSpace[i] = m - caveM
    minVoidSpace = min(minVoidSpace, voidSpace[i])
    sumVoidSpace += voidSpace[i]

print(max(i[0] for i in voidSpace.items() if i[1] == minVoidSpace),
      sum(i[1] for i in voidSpace.items()))