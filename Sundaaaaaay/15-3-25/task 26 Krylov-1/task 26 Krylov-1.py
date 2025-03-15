with open("26var01.txt") as f:
    # with open("test") as f:
    n, m, k = map(int, f.readline().split())
    data = [list(map(int, i.split())) for i in f]

base = [m + 1] * k

for h, v in data:
    base[v - 1] = min(base[v - 1], h)

ans = []

for i in range(len(base) - 1):
    if base[i] <= base[i + 1]:
        ans.append([base[i] - 1, i + 1])
    if base[i] > base[i + 1]:
        ans.append([base[i + 1] - 1, i + 1])

ans = sorted(ans, key=lambda x: (-x[0], x[1]))

print(*ans[0])
