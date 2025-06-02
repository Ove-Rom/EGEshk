with open("26_21588.txt") as f:
    n, k = map(int, f.readline().split())
    data = [list(map(int, i.split())) for i in f]

data = sorted(data, key=lambda x: [-x[0],[1], x[2]])

for target in data:
    