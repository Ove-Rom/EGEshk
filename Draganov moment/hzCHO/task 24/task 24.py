with open("24v1.txt") as f: data = f.read()

for i in "VXZ":
    data = data.replace(i, " ")

data = data.split()

ans = []

for i in data:
    if all(i.count(j) <= 8 for j in "AEIOUY"):
        ans.append(len(i))

print(max(ans))