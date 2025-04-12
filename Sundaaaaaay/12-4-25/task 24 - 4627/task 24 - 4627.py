from re import finditer

with open("24_4627.txt") as f:
    data = f.read()

pat = r"(NPO|PNO)*"

base = finditer(pat, data)

lines = [i.group() for i in base]

print(len(max(lines, key=len))//3)