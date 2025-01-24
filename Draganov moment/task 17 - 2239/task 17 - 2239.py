with open("17_2239.txt") as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if i % 19 == 0)
minn = 999999999
count = 0

for i in range(len(data) - 1):
    if data[i] > maxx or data[i+1] > maxx:
        count += 1
        minn = min(minn, data[i] + data[i+1])

print(count, minn)