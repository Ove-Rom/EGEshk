with open("26_18967.txt") as f:
    n, k = map(int, f.readline().split())
    data = [list(map(int, i.split())) for i in f]

free = n
sadCount = 0
sadList = []

data = sorted(data, key=lambda x: (x[1], x[0]))

sdali = []
full = []

for group in data:
    if group[0] in sadList: continue
    if free:
        svobodnoVnachale = True
    else:
        svobodnoVnachale = False
    if group[0] in sdali:
        free += group[2]
    elif free - group[2] >= 0:
        free -= group[2]
        sdali.append(group[0])
    else:
        sadCount += group[2]
        sadList.append(group[0])
    if not free and svobodnoVnachale: full.append([group[1]])
    if free and not svobodnoVnachale: full[-1].append(group[1])

time = 0

for i in range(len(full)):
    if len(full[i]) == 1:
        time += 1
    else: time += full[i][-1] - full[i][0]

print(sadCount, time)
