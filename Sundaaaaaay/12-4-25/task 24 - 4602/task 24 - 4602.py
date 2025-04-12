from re import finditer

with open("24_4602.txt") as f:
    data = f.read()

for g in "AO":
    data = data.replace(f"{g}", "g")

for s in "BCD":
    data = data.replace(f"{s}", "s")

pat = r"(sg)*"

lines = finditer(pat, data)

mat = [i.group() for i in lines]

print(len(max(mat, key=len)) // 2)
