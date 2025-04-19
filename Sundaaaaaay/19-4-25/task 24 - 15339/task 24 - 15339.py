from re import *

with open("24_15339.txt") as f:
    data = f.read()

pattern = r"(\D\d)+\D?|(\d\D)+\d?"

lines = finditer(pattern, data)

ans = []

for i in lines:
    s = i.group()
    # print(s)
    ans.append(s)

# print(max(ans, key=len))
print(len(max(ans, key=len)))
