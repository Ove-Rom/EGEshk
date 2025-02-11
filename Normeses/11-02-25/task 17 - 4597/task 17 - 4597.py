with open("17_4597.txt") as f:
    data = [int(i) for i in f]

minN = min(data)

count = 0
maxCount = 0

for i in range(len(data) - 1):
    if data[i] % 117 == minN or data[i+1] % 117 == minN:
        count+= 1
        maxCount = max(maxCount, data[i]+data[i+1])

print(count, maxCount)