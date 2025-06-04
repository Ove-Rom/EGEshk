from itertools import product

c = 0

for i in product("gepard", repeat=5):
    s = "".join(i)
    c1 = s.count("g") == 1
    c2 = s[0] != "a"
    c3 = s[-1] != "e"
    if c1 and c2 and c3:
        c += 1

print(c)