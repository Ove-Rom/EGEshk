from re import *
with open("24_18284.txt") as f:
    data = f.read()

pattern = r"L[^L]*?O.*?V.*?E"

lines = finditer(pattern, data)

ans = []

for i in lines:
    ans.append(len(i.group()))

print(min(ans))