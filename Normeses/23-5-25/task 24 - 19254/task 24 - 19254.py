with open("24_19254.txt") as f:
    data = f.read()

data = data.split("FSRQ")
ans = []
for i in range(len(data)-80):
    s = "".join(data[i:i+81])
    ans.append(len(s) + 80*4 + 6)

print(max(ans))