from string import ascii_uppercase

with open("24_14510.txt") as f:
    data = f.read()

gl = "AEIOUY"

for i in ascii_uppercase:
    if i in gl:
        data = data.replace(i, "g")
    else: data = data.replace(i, "s")

data = data.replace("ssg", "ssg ").split()

ans = []

for i in range(len(data) - 499):
    s = 0
    for j in range(i, i + 499):
        s += len(data[j])
    ans.append(s)

print(min(ans)+3)