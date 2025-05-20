with open("24_19489.txt") as f:
    data = f.read()

data = data.replace("WSFWW", "WSFW SFWW")

data = data.split()
ans = []

for i in data:
    if i.count("WWF") <= 120:
        ans.append(len(i))
        continue
    s = i.split("WWF")
    for j in range(len(s) - 120):
        l = "".join(data[j:j + 101])
        ans.append(len(l) + 364)

print(max(ans))