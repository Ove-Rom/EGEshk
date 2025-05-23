with open("24_21717.txt") as f:
    data = f.read()

data = data.split("RSQ")
ans = []
for i in range(len(data) - 128):
    s = "RSQ".join(data[i:i+129])
    ans.append(len(s)+7)

print(min(ans))