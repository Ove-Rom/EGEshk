with open("26_9171.txt") as f:
    m, k, n = map(int, f.readline().split())
    data = [list(map(int, i.split())) for i in f]

base = dict()
data = sorted(data, key=lambda x: (x[0], -x[1]))

for i in data:
    if i[0] not in base:base[i[0]] = [i[1]]
    else:base[i[0]].append(i[1])

free = k
inTrain = []
full = [0] * m
haypuyushiye = 0

for station in range(1, m):
    while station in inTrain: inTrain.remove(station); free += 1; haypuyushiye += 1
    if station in base:
        for stop in base[station]:
            if free: inTrain.append(stop); free -= 1
    if not free:
        for i in range(station, m): full[i] = 1
    if free:
        for i in range(station, m): full[i] = 0

print(haypuyushiye, sum(full))
