with open("17_9748.txt") as f: data = [int(i) for i in f]

maxN = max(i for i in data if i % 100 == 15)

count = 0
maxCount = 0

for i in range(len(data) - 2):
    c1 = len(str(data[i])) == 4
    c2 = len(str(data[i + 1])) == 4
    c3 = len(str(data[i + 2])) == 4
    if c1 ^ c2 ^ c3 and not (c1 & c2 & c3):
        if sum(data[i:i + 3]) >= maxN:
            count += 1
            maxCount = max(maxCount, sum(data[i:i + 4]))

print(count, maxCount)
