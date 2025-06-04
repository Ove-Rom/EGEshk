from itertools import product

c = 0

for i in product("01234567", repeat=5):
    s = " " + "".join(i) + " "
    if s[1] == "0": continue
    c1 = s.count("6") == 1
    six = s.find("6")
    c2 = s[six-1] not in "1357" and s[six+1] not in "1357"
    if c1 and c2:
        c += 1

print(c)