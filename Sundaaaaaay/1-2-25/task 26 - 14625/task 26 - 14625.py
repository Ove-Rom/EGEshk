with open("26_14625.txt") as f:
    f.readline()
    k, r, m = f.readline().split()
    data = [[int(i.split()[0]), int(i.split()[1]), i.split()[2]] for i in f]

k = int(k)
r = int(r)
m = int(m) * 2 ** 20

# data = sorted(data, key = lambda x: x[1] * 2**20 if x[-1] == "mb" else x[1] * 2**10 if x[-1] == "kb" else x[1])

for i in range(len(data)):
    if data[i][-1] == "mb":
        data[i] = [data[i][0], data[i][1] * 2 ** 20]
    elif data[i][-1] == "kb":
        data[i] = [data[i][0], data[i][1] * 2 ** 10]
    else:
        data[i] = [data[i][0], data[i][1]]

data = sorted(data, key=lambda x: x[-1], reverse=True)

trashedCount = [0 for i in range(k)]
trashedSum = 0
minTrashed = 0

for i in data:
    if trashedSum + i[1] >= m:
        for j in data[::-1]:
            if trashedCount[i[0] - 1] < r:
                if trashedSum + j[1] >= m:
                    trashedCount[i[0] - 1] += 1
                    minTrashed = j[1]
                    print(sum(l for l in trashedCount), minTrashed)
                    exit(80085)
    if trashedCount[i[0] - 1] < r:
        trashedCount[i[0] - 1] += 1
        trashedSum += i[1]