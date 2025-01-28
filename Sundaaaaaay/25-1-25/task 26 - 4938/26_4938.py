with open("26_4938.txt") as f:
    maxTime = int(f.readline().split()[0])
    data = [[int(i.split()[0]), int(i.split()[1])] for i in f]

data = sorted(data, key=lambda x: x[1])

start = [data[0]]

for i in data:
    if start[-1][1] <= i[0]:
        start.append(i)

print(len(start), start[-1][0])


