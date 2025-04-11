with open("26_8512.txt") as f:
# with open("test") as f:
    k = int(f.readline())
    n = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

count = 0
lastCell = 0

data = sorted(data)

cells = [0]*k

for start, end in data:
    for i in range(len(cells)):
        if cells[i] < start:
            cells[i] = 0
    if 0 in cells:
        count += 1
        lastCell = cells.index(0)+1
        cells[lastCell-1] = end

print(count, lastCell)


