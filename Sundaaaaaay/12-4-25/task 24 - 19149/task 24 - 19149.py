from re import finditer

with open("24_19149.txt") as f:
    data = f.read()

p = r"[(](\d+|([(]\d+[+]\d+[)]))([+](\d+|([(]\d+[+]\d+[)])))*[)]"

base = finditer(p, data)

lines = [i.group() for i in base]

print(len(max(lines, key=lambda x: len(x) if eval(x) % 2 == 0 else 0)))