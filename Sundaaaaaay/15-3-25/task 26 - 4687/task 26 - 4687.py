with open("26_4687.txt") as f:
    # with open("test") as f:
    n, k = map(int, f.readline().split())
    data = [list(map(int, i.split())) for i in f]

stage1 = []
stage2 = []

nRows = max(data, key=lambda x: x[1])[1]

for i in range(nRows):
    stage1.append(['x'] + ["0"] * (k - 2) + ['x'])
    stage2.append(['x'] + ["0"] * (k - 2) + ['x'])

for i in data:
    match i[0]:
        case 1:
            stage1[i[1] - 1][i[2] - 1] = "1"
        case 2:
            stage2[i[1] - 1][i[2] - 1] = "1"

ans = []

for i in range(nRows):
    if stage1[i] != ['x'] + ["0"] * (k - 2) + ['x'] and "0000" in ''.join(stage1[i]):
        ans.append(i + 1)
    if stage2[i] != ['x'] + ["0"] * (k - 2) + ['x'] and "0000" in ''.join(stage2[i]):
        ans.append(i + 1)

print(max(ans), len(ans))
