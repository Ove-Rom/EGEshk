from re import finditer

with open("24_17563.txt") as f:
    data = f.read()

p = r"(([789][0789]*)[*-])*([789][0789]*)"

base = finditer(p, data)

lines = [i.group() for i in base]

print(len(max(lines, key=len)))
