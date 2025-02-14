with open("17_7716.txt") as f: data = [int(i) for i in f]

maxN = max(i for i in data if all(int(j) % 2 != 0 for j in str(i)))
ans = []

for i in range(len(data) - 1):
    c1 = all(int(j) % 2 == 0 for j in str(data[i]))
    c2 = all(int(j) % 2 == 0 for j in str(data[i+1]))
    c3 = data[i] + data[i+1] > maxN
    if (c1 or c2) and c3: ans.append(data[i] + data[i+1])

print(len(ans), max(ans))