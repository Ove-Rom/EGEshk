from re import *

with open("24_1866.txt") as f:
    data = f.read()

p = r"(?<=ad|da)\w+?(?=ad|da)"

base = findall(p, data)

print(len(max(base, key=len)) + 2)