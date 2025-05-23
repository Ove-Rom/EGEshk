from re import finditer

with open("24_17878.txt") as f:
    data = f.read()

n = r"([1-9]\d*|0)"
pat = rf"({n}[-*])+{n}"
ans = []
for i in finditer(pat, data):
    ans.append(len(i.group()))

print(max(ans))

