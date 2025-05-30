with open("26_3586.txt") as f:
    n = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

data = sorted(data)

maxLine = maxN = 0

for l, r in zip(data, data[1:]):
    if l[0] != r[0]: continue
    Δ = r[1] - l[1] - 1
    if Δ >= maxN:
        maxN = Δ
        maxLine = l[0]

print(maxLine, maxN)