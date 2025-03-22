from itertools import groupby

with open("26_4553.txt") as f:
    n = int(f.readline())
    data = [list(map(int, i.split()[:-1])) + [i.split()[-1]] for i in f]

screen = []

for i in range(10_001):
    screen.append(['-']*10_001)

for i in data:
    screen[i[0]][i[1]] = i[2]

ans = []

for i in range(10_000):
    l = [len(list(group)) for letter, group in groupby(screen[i]) if letter == '+']
    if l:
        ans.append([max(l), i])

print(*max(ans))
