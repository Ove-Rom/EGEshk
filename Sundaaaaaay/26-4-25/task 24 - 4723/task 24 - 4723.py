from re import *

with open("24-186.txt") as f:
    data = f.read()

pat = r"(?<=\D)7\d{10}(?=\D)"

ans = 0

for i in finditer(pat, data):
    s = i.group()
    c1 = int(s[0]) + int(s[1])
    c2 = int(s[-2]) + int(s[-1])
    if c1 == c2:
        ans += 1

print(ans)