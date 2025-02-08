with open("26_8512.txt") as f:
    k = int(f.readline())
    n = int(f.readline())
    data = [[int(i.split()[0]), int(i.split()[1])] for i in f]

data = sorted(data)
print(data)

cells = [0] * k

count = 0
mxNum = 0

for start, stop in data:
    for i in range(len(cells)):
        if cells[i] < start:
            cells[i] = 0
    if 0 in cells:
        count += 1
        mxNum = cells.index(0)+1
        cells[cells.index(0)] = stop

print(count, mxNum)
