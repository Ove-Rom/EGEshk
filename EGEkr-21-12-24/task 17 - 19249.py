with open("17_19249.txt") as file:
    data = file.read().split("\n")

count = 0
minS = 10 ** 10
maxN = 0

for i in data:
    if len(str(abs(int(i)))) == 5 and i[-2:] == "43":
        maxN = max(maxN, int(i))
maxN *= maxN

for i in range(len(data)-2):
    c1 = any(len(str(abs(int(data[j])))) == 5 and data[j][-2:] == "43" for j in range(i, i+3))
    c2 = sum(int(data[j])**2 for j in range(i, i+3)) <= maxN
    if c1 & c2:
        count += 1
        minS = min(minS, sum(int(data[j])**2 for j in range(i, i+3)))
print(count, minS)