from itertools import groupby

# with open("test") as f:
with open("26_9847.txt") as f:
    n = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

timeline = [0] * 1440

for arrival, departure in data:
    for time in range(arrival, departure):
        timeline[time] += 1

maxN = max(timeline)
count  = 0

for num, pos in groupby(timeline):
    count += num == maxN

print(count, maxN)