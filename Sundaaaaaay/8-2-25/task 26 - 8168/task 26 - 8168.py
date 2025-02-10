with open("26_8168.txt") as f:
    k = int(f.readline())
    n = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

data = sorted(data, key=lambda x: (x[0], x[1]))
sadCount = 0
ans = [0] * 24 * 60
cells = [0] * k

for start, stop in data:
    for i in range(len(cells)):
        if cells[i] < start:
            cells[i] = start + stop
            for j in range(start + 1, start + stop):
                ans[j] += 1
            break
    else:
        sadCount += 1

print(sadCount, ans.count(k))
