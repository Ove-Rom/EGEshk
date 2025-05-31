with open("26_7626.txt") as f:
    k = int(f.readline())
    n = int(f.readline())
    data = sorted(list(map(int, i.split())) for i in f)

cells = [0] * k
lastCell = 0
count = 0

for start, stop in data:
    for i in range(k):
        if cells[i] < start:
            cells[i] = stop
            lastCell = i + 1
            count += 1
            break

print(count, lastCell)