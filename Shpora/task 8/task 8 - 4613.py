from itertools import product

c = 0

for i in product("012345678", repeat=5):
    s = "".join(i)
    if s[0] in "01357":continue
    c1 = s[-1] not in "18"
    c2 = s.count("3") <= 1
    if c1 and c2:
        c += 1

print(c)