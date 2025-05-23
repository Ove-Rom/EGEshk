from re import finditer

with open("24_6798.txt") as f:
    data = f.read()

pat = r"([CDF].[AO])+"
ans = []
for i in finditer(pat, data):
    ans.append(len(i.group())//3)

print(max(ans))