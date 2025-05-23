from re import finditer

with open("24_21421.txt") as f:
    data = f.read()

pat = r"[1-9AB][\dAB]+[02468B]"

ans = []

for i in finditer(pat, data):
    ans.append(len(i.group()))

print(max(ans))