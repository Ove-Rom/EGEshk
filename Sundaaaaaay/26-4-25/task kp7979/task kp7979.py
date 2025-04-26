from re import *

with open("24-314.txt") as f:
    data = f.read()

n = r"[1-7][0-7]*"

pat = fr"(?<=F)(0[+*])?({n}[+*])+0|({n})"

ans = []

for i in finditer(pat, data):
    ans.append((i.group()))

m = max(ans, key=len)
print(m)
s = 0
muls = m.split("+")
print(muls)

for i in muls:
    m = 1
    for n in i.split("*"):
        m *= int(n, 8)
    s += m

print(s)