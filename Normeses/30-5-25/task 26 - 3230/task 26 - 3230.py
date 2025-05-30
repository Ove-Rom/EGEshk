with open("26_3230.txt") as f:
    n = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

data = sorted(data)

maxLine = 0
minRow = float("inf")

for l, r in zip(data, data[1:]):
    if l[0] != r[0]: continue
    if r[1] - l[1] == 12:
        maxLine = l[0]
        minRow = min(minRow, l[1]+1)

print(maxLine, minRow)