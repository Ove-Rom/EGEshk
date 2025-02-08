data = open("24_19968.txt").read()

data = data.replace("**", " ").replace("++", " ")
data = data.replace("*+", " ").replace("+*", " ")
data = data.replace("+0", " 0")

for i in "6789ABCDEF":
    data = data.replace(i, " ")

for i in "012345":
    data = data.replace(f"+0{i}", " ")

for i in "012345":
    while f" 0{i}" in data:
        data = data.replace(f" 0{i}", f" 0 {i}")

print(max(data, key=len))