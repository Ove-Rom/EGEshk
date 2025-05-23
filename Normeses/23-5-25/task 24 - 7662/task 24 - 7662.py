with open("24_7662.txt") as f:
    data = f.read()

data = data.split("SOLO")
ans = []
for i in range(len(data) - 4):
    l = "".join(data[i:i + 5])
    if len([1 for j in set(l) if j in "0123456789"]) >= 5:
        ans.append(len(l) + 6 + 16)

print(max(ans))
