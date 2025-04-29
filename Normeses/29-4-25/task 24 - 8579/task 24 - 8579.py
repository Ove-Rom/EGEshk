from re import finditer
from weakref import finalize

with open("24_8579.txt") as f:
    data = f.read()

for i in "2468":
    data = data.replace(i, "0")
for i in "3579":
    data = data.replace(i, "1")

pet = r"(0[A-Z]+1)|(1[A-Z]+0)"

ans = []

for i in finditer(pet, data):
    ans.append(len(i.group()))

print(max(ans))