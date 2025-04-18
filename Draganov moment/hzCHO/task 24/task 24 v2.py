with open("24v1.txt") as f: data = f.read()

for i in "XY":
    data = data.replace(i, " ")

data = data.split()

ans = []

for i in data:
    if all(i.count(j) <= 10 for j in "SUN"):
        ans.append(len(i))

print(max(ans))