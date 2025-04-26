with open("24-333.txt") as f:
    data = f.read()

from re import *

y = "@yandex\.ru"
g = "@gmail\.com"

pat = rf"\w[.\w]+\w({y}|{g})"

ans = []

for l in finditer(pat, data):
    s = l.group()
    ans.append([len(s), s])

print(max(ans))