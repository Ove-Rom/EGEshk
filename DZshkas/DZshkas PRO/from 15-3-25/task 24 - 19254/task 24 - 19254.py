data = data2 = open("24_19254.txt").read()

data = data.split("FSRQ")

base = []

for i in data:
    base.append(len(i))

print(max(sum(base[i:i + 81]) + 4 * 80 + 6 for i in range(len(base) - 80)))

cords = []
ans = []

for i in range(len(data2) - 3):
    if data2[i:i + 4] == "FSRQ":
        cords.append(i + 1)

for i in range(len(cords) - 81):
    ans.append((cords[i + 81] + 2 - cords[i]))

print(max(ans))
