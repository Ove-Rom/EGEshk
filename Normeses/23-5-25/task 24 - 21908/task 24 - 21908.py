from re import finditer

with open("24_21908.txt") as f:
    data = f.read()

pat = r"[1-9ABCD][\dABCD]+[02468BD]"

ans = []

for i in finditer(pat, data):
    ans.append(len(i.group()))

print(max(ans))