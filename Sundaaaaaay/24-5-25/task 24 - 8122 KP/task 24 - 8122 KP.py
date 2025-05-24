from re import finditer

with open("24-347.txt") as f:
    data = f.read()

pat = r"[1-9AB][\dAB]*[02468A]"
ans = []
for i in finditer(pat, data):
    s = i.group()
    if int(s, 12) % 3 == 0:
        ans.append(s)
        continue
    for l in range(len(s)):
        for r in range(len(s)+1, l, -1):
            p = s[l:r].lstrip("0")
            if p and int(p, 12) % 3 == 0:
                ans.append(p)
                break

m = max(ans, key=len)
print(data.find(m) + len(m) - 1)
