from re import finditer

with open("24_3792.txt") as f:
    data = f.read()

# data = data.replace("D", " ").replace("E", " ")
#
# print((max(data.split(), key=len)))

pat = r"[ABC]+"

lines = finditer(pat, data)
ans = []
for i in lines:
    ans.append(len(i.group()))

print(max(ans))