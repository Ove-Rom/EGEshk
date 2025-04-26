with open("24-337.txt") as f:
    data = f.read()

from re import *

pat = r"1[\dA-D]+"

lines = finditer(pat, data)

ans = []

for l in lines:
    s = l.group()
    if int(s, 14) % 7 == 0:
        ans.append(len(s))
    else:
        for j in range(len(s)):
            if s[j] != "1": continue
            for k in range(j + 1, len(s)):
                if int(s[j:k+1], 14) % 7 == 0:
                    ans.append(len(s[j:k+1]))

print(max(ans))