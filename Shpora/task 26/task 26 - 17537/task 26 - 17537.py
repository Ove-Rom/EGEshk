with open("26_17537.txt") as f:
    n, m, k = map(int, f.readline().split())
    data = [list(map(int, i.split())) for i in f]

p = [m + 1] * k
maxRow = maxCol = 0

for row, col in data:
    p[col] = min(p[col], row)

for i in range(k-1):
    if maxRow <= min(p[i]-1, p[i+1]-1):
        maxRow = min(p[i]-1, p[i+1]-1)
        maxCol = i+1

print(maxRow, maxCol)
