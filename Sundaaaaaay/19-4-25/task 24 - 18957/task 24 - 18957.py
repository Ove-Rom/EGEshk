from re import *
with open("24_18597.txt") as f:
    data = f.read()

pattern = r"[1-9]\d{3}\.\d+&[1-9]\d{3}\.\d+"

lines = finditer(pattern, data)

ans = []

for i in lines:
    ans.append(len(i.group()))

print(max(ans))