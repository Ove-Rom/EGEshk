with open("24_20909.txt") as f:
    data = f.read()

data = data.split("AB")

ans = []

for i in range(len(data) - 100):
    s = "".join(data[i:i+101])
    ans.append(len(s) + 202)

print(max(ans))