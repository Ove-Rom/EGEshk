with open("26.2_19727.txt") as f:
    maxMass = int(f.readline().split()[0])
    data = [int(i) for i in f]

data = sorted(data)

n = 0
Mass = 0

for i in data:
    if Mass + i <= maxMass:
        Mass += i
        n += 1
print(n)

critMass = sum(data[:n - 1])
c = 0

for i in data[::-1]:
    if critMass + i > maxMass:
        c += 1

print(c)
