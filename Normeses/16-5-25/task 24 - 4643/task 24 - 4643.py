from re import finditer

with open("24_4643.txt") as f:
    data = f.read()

pat = r"(\d\d\D)+"
ans = []
for i in finditer(pat, data):
    ans.append(len(i.group()))

print(max(ans)//3)