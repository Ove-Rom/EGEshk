from itertools import product

c = 0

for i in product("0123456", repeat=5):
    d = "".join(i).lstrip("0")
    if len(d) == 5:
        s = "".join(str(int(j) % 2) for j in d)
        c1 = s.count("00") >= 2
        c2 = "000" not in s
        if c1 and c2:
            c += 1

print(c)