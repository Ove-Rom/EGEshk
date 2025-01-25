with open("26_17786.txt") as f:
    n, v = map(int, f.readline().split())
    data = [int(i) for i in f]

data = sorted(data)

minM = min(i for i in data if i >= 7000)
maxM = max(i for i in data if i <= 12000)
minMp = data.index(minM)
maxMp = data.index(maxM)

arbuzi = data[minMp:maxMp+1][::-1]

maxMass = 0
count = 0
minMass = 0
for mass in arbuzi:
    if maxMass + mass <= v*1000:
        maxMass += mass
        minMass = mass
        count += 1

print(count, minMass)