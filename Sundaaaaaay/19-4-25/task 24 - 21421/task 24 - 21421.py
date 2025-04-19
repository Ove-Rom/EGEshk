from re import *
with open("24_21421.txt") as f:
    data = f.read()

pattern = r"[1-9AB][\dAB]*[02468A]"

lines = finditer(pattern, data)

ans = []

for i in lines:
    ans.append(len(i.group()))

print(max(ans))