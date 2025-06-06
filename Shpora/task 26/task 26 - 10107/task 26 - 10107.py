with open("26_10107.txt") as f:
    n = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

data = sorted(data, key=lambda x: [x[1], -x[0]])

toDo = [data[0]]

for start, stop in data:
    if start >= toDo[-1][1]:
        toDo.append([start, stop])

print(len(toDo), toDo[-1][0] - toDo[-2][1])
