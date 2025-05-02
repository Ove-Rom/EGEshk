from itertools import product

c = 0

for i in product("012345678", repeat=7):
    if len(s := "".join(i).lstrip("0")) == 7:
        c1 = s[0] not in "1357"
        c2 = int(s[-1]) % 3
        c3 = "6" in s
        if c1 and c2 and c3:
            c += 1

print(c)
