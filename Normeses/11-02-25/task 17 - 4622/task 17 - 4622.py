with open("17_4622.txt") as f: data = [int(i) for i in f]

minN = min(i for i in data if i % 19 == 0 and i > 0)

count = 0
absCount = 0

for i in range(len(data)-1):
    if data[i] + data[i+1] < minN:
        count+= 1
        absCount = max(abs(data[i] + data[i+1]), absCount)

print(count, absCount)