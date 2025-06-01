# with open("test") as f:
with open("26_9793.txt") as f:
    f.readline()
    data = []
    num = 1
    for i in f:
        sh, ok = map(int, i.split())
        data += [[num, True, sh]] + [[num, False, ok]]
        num += 1

data = sorted(data, key=lambda x: x[2])
conveyor = []
last = count = 0

for n, t, time in data:
    if n in conveyor: continue
    if t:
        conveyor.append(n)
        count += 1
        last = [n, True]
    else:
        conveyor.append(n)
        last = [n, False]

print(last[0], count - last[-1])
