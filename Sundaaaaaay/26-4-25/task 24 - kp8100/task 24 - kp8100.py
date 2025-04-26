with open("24-335.txt") as f:
    data = f.read()

from re import *

A = r"[1-9]\d*[^05\-+()]"
B = r"[1-9]\d*[05]"

pat = rf"(\({A}[+-]{B}\))*"

lines = finditer(pat, data)
ans = []

for l in lines:
    ans.append(len(l.group()))

print(max(ans))