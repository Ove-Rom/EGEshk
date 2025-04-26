from re import *

with open("24-332.txt") as f:
    data = f.read()

pat = r"[A-C][a-c]*( [A-C]?[a-c]+)*\."

ans = []

for l in finditer(pat, data):
    s = l.group()
    ans.append([len(s), s])

print(max(ans))