from itertools import permutations

with open("24_8510.txt") as f:
    data = f.read()

for i in permutations("PNO", 2):
    data = data.replace(''.join(i), '*')

while "*P" in data or "*N" in data or "*O" in data or "P*" in data or "N*" in data or "O*" in data:
    for i in "PNO":
        data = data.replace(f"*{i}", '*').replace(f"{i}*", '*')

data = data.split('*')

maxLen = 0

for i in range(len(data)-2):
    maxLen = max(len(data[i]) + len(data[i+1]) + len(data[i+2]), maxLen)

print(maxLen)