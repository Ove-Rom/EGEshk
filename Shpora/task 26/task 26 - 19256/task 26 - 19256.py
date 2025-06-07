from itertools import groupby

with open("26_19256.txt") as f:
    n = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

data.sort()
bestStudent = count = 0

for ID, info in groupby(data, key=lambda x: x[0]):
    tasks = sorted(set(i[1] for i in info))
    s = 1
    sums = [0]
    for i in range(len(tasks) - 1):
        if tasks[i + 1] - tasks[i] == 1:
            s += 1
        else:
            s = 1
        sums.append(s)
    if max(sums) > count:
        count = max(sums)
        bestStudent = ID

print(bestStudent, count)
