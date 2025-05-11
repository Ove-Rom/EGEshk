from itertools import groupby

with open("26_9847.txt") as f:
    n = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

base = [0]*1441

for start, stop in data:
    for i in range(start, stop):
        base[i] += 1

# with open("output", "w") as o:
#     for n, c in enumerate(base):
#         o.write(f"{n};{c}\n")

maxN = max(base)
c = 0

for symb, line in groupby(base):
    if symb == maxN: c += 1

print(c, maxN)
