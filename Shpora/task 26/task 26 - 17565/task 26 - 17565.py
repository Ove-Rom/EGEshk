from itertools import groupby

with open("26_17565.txt") as f:
    n, s = map(int, f.readline().split())
    data = []
    for i in f:
        id, e1, e2, e3, sob = map(int, i.split())
        data.append([id, e1 + e2 + e3, sob])

data.sort(key=lambda x: [-x[1], -x[2], x[0]])
lastID = ans = 0

for grade, info in groupby(data, key=lambda x: x[1]):
    info = list(info)
    if grade == data[s - 1][1]:
        ans = len(list(info))
        break
    else: lastID = list(info)[-1][0]

print(lastID, ans)