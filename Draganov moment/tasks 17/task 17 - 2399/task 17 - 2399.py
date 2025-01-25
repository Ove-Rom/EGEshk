with open("17_2399.txt") as file:
    data = [int(i) for i in file]

count = 0
minS = 999999999999

maxx = sum([int(j) for i in [str(i) for i in data if i % 35 == 0] for j in i])

for i in range(len(data) - 1):
    c1 = data[i] > maxx
    c2 = data[i+1] > maxx
    if c1 and not c2:
        if hex(data[i+1])[-2:] == 'ef':
            count+=1
            minS = min(minS, data[i] + data[i+1])
    if not c1 and c2:
        if hex(data[i])[-2:] == 'ef':
            count+=1
            minS = min(minS, data[i] + data[i+1])

print(count, minS)