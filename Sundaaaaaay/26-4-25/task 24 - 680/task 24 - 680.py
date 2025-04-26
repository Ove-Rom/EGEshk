from re import *

with open("24-271.txt") as f:
    data = f.read()

pat = r"#[\dA-F]{6}"

c = 0

for l in finditer(pat, data):
    s = l.group()
    r = int(s[1:3], 16)
    g = int(s[3:5], 16)
    b = int(s[5::], 16)
    if g < r > b:
        c += 1

print(c)