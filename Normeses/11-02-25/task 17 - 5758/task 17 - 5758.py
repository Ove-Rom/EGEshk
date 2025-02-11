from itertools import combinations

with open("17_5758.txt") as f: data = [int(i) for i in f]

mods = [data.count(i) for i in range(-1000, 1001)]
moda = mods.index(max(mods)) - 1000

ans = []

for i in range(len(data) - 1):
    for j in range(i+2, len(data), 2):
        if min(data[i], data[j]) < moda < max(data[i], data[j]):
            ans.append(max(moda - data[i], moda - data[j]))

print(len(ans), max(ans))
