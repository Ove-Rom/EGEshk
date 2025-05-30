with open("26_1868.txt") as f:
    n = int(f.readline())
    data = [list(map(int, i.split())) for i in f]

data = sorted(data, key=lambda x: [-x[0], x[1]])

for l ,r in zip(data, data[1:]):
    if l[0] != r[0]: continue
    if r[1] - l[1] == 3:
        print(l[0], l[1]+1)
        break
