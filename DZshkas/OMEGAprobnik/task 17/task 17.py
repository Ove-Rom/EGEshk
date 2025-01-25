with open("17_8562.txt") as file:
    data = [int(i) for i in file]

minn = min(i for i in data if len(str(abs(i))) == 2 and str(i)[-1] == '1') ** 2

count = 0
minS = 99999999999

for i in range(len(data) - 1):
    c1 = data[i] ** 2 < minn <= data[i + 1] ** 2
    c2 = data[i+1] ** 2 < minn <= data[i] ** 2
    c3 = data[i] + data[i+1] >= 0
    if (c1 | c2) & c3:
        count += 1
        minS = min(minS, data[i] + data[i+1])

print(count, minS)