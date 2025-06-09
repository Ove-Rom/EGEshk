from itertools import groupby

with open("26_19752.txt") as f:
    n = int(f.readline())
    data = []
    for i in f:
        info = list(map(int, i.split()))
        ID = info[0]
        balls = info[1:]
        if sum(balls) <= 0: continue
        data.append([ID,
                     [sum(balls),  # сумма баллов
                      sum(j for j in balls if j > 0),  # сумма плюсов
                      sum(j != 0 for j in balls)]])  # количество ответов

data.sort(key=lambda x: [-x[1][0], -x[1][1], -x[1][2], x[0]])

nextCount = len(data) // 3

for n, pos in groupby(data.copy(), key=lambda x: x[1]):
    pos = list(pos)
    nextCount -= len(pos)
    for i in pos:
        data.remove(i)
    if nextCount <= 0: break

dopTour = []
dopCount = len(data) // 10

for n, pos in groupby(data.copy(), key=lambda x: x[1]):
    pos = list(pos)
    dopCount -= len(pos)
    dopTour += list(pos)
    if dopCount <= 0: break

print(dopTour[0][0], len(dopTour))
