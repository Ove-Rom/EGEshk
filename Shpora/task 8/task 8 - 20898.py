from itertools import product

count = 0

for i in product("012345678", repeat = 5):
    s = " " + "".join(i) + " "
    if s[1] == "0": continue
    c1 = s.count("0") == 1
    zero = s.find("0")
    c2 = s[zero-1] not in "1357" and s[zero+1] not in "1357"
    if c1 and c2:
        count += 1

print(count)