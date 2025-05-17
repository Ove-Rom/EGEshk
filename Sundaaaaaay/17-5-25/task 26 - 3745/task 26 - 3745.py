with open("26_3745.txt") as f:
    n = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

ans = dict()
c = 0

for line in range(1, 78):
    for col in range(1, 80):
        if [line, col] in data:
            if (all(i in data for i in (
                    [line, col + 1],
                    [line + 1, col],
                    [line + 1, col + 1]
            )) and all(i not in data for i in (
                    [line - 1, col],
                    [line - 1, col + 1],
                    [line, col - 1],
                    [line, col + 2],
                    [line + 1, col - 1],
                    [line + 1, col + 2],
                    [line + 2, col],
                    [line + 2, col + 1]
            ))):
                if line not in ans:
                    ans[line] = 1
                else:
                    ans[line] += 1
                if line + 1 not in ans:
                    ans[line + 1] = 1
                else:
                    ans[line + 1] += 1
                c += 1

print(c, max(ans.items(), key=lambda x: x[1])[0])
