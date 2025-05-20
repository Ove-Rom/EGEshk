from re import finditer

with open("24_15339.txt") as f:
    data = f.read()

pat = r"\D?(\d\D)+\d?"
ans = []
for i in finditer(pat, data):
    ans.append(len(i.group()))

print(max(ans))