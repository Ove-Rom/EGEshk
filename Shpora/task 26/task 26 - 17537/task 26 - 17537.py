with open("26_17537.txt") as f:
    n, m, k = map(int, f.readline().split())
    p = [m + 1] * (k + 1)
    for i in f:
        row, col = map(int, i.split())
        p[col] = min(p[col], row - 1)

maxRow = maxCol = 0

for i in range(1, k):
    if maxRow <= min(p[i], p[i + 1]):
        maxRow = min(p[i], p[i + 1])
        maxCol = i + 1

print(maxRow, maxCol)
