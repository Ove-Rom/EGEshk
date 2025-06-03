from itertools import product

count = 0

for i in product("01234567", repeat=5):
    s = "".join(i)
    if s[0] == "0": continue
    c1 = s[0] not in "1357"
    c2 = s[-1] not in "26"
    c3 = s.count("7") <= 2
    if c1 and c2 and c3:
        count += 1

print(count)