from re import finditer

with open("24-335.txt") as f:
    data = f.read()

a = r"(([1-9]\d*)?[1-46-9])"
b = r"(([1-9]\d*)?[05])"
pat = rf"(\({a}[+-]{b}\))+"
ans = []
for i in finditer(pat, data):
    ans.append(len(i.group()))

print(max(ans))