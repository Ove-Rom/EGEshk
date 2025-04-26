from re import *
from collections import *

with open("24-235.txt") as f:
    data = f.read()

ans = {i:0 for i in "XYZWOP"}

for l in finditer(r"X.P", data):
    ans[l.group()[1]] += 1

print(max(ans.values()))