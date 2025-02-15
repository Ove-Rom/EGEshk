with open("26.txt") as f:
# with open("test") as f:
    f.readline()
    data = [(int(i.split()[0]), int(i.split()[1]) + int(i.split()[0])) for i in f]

data = sorted(data, key=lambda x: x[1])

start = [data[0]]

for i in data:
    if start[-1][1] <= i[0]:
        start.append(i)
print(len(start),start[-1][0] - start[-2][1])