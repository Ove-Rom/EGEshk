from string import ascii_uppercase, digits

with open("24_19967.txt") as f:
    data = f.read()

data = data.replace("AFD", "@")

data = data.replace("+*", " ").replace("*+", " ")
data = data.replace("++", " ").replace("**", " ")
for i in digits:
    data = data.replace(f"+0{i}", f"+0 {i}").replace(f"*0{i}", f"+0 {i}")

for i in ascii_uppercase[:6]:
    data = data.replace(i, " ")

data = data.replace("@", "AFD")

data = data.split()

for i in range(len(data)):
    for j in range(3):
        data[i] = data[i].strip()
        data[i] = data[i].strip("*")
        data[i] = data[i].strip("+")

ans = []

for i in data:
    if i[:3] == "AFD":
        ans.append(i)

print(len(max(ans, key=len)))
