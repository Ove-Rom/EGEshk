with open("26_10107.txt") as f:
    f.readline()
    data = [(int(i.split()[0]), int(i.split()[1])) for i in f]

data = sorted(data, key = lambda x: x[1])

haypuem = [data[0]]

for i in data:
    if haypuem[-1][1] <= i[0]:
        haypuem.append(i)

print(len(haypuem), haypuem[-1][0] - haypuem[-2][1])

