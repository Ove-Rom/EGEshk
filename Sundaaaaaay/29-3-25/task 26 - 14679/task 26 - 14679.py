from itertools import groupby

with open("26_14679.txt") as f:
    n = int(f.readline())
    k = int(f.readline())
    data = [[list(map(int, i.split()[0].split('.'))),
             list(map(int, i.split()[1].split('.')))]
            for i in f]

line = [0] * (60 * 24 * 30 * 36 + 1)

for start, stop in data:
    t1 = start[0] * 24 * 60 + \
         start[1] * 30 * 24 * 60 + \
         start[2] * 60 + \
         start[3]
    t2 = stop[0] * 24 * 60 + \
         stop[1] * 30 * 24 * 60 + \
         stop[2] * 60 + \
         stop[3]
    # print(start, stop)
    for moment in range(t1, t2 + 1):
        line[moment] += 1

c = 0

for i, j in groupby(line, key=lambda x: x >= k):
    if i: c += 1

print(c, max(line))
