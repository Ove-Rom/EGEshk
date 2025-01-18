with open("26_4604.txt") as file:
    file.readline()
    data = [int(i) for i in file]

data = sorted(data)[::-1]

minS = data[0]
count = 1
# data = [43, 40, 40, 32, 30]
# print(data)
for i in range(len(data)):
    if minS - data[i] >= 3:
        minS = data[i]
        count += 1

print(count, minS)
