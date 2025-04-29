from itertools import product

c = 0

for i in product("01234567", repeat=6):
    s = "".join(i).lstrip("0")
    if s:
        c1 = len(s) == 6
        l = [int(j) % 2 for j in s]
        c2 = not any(j in l for j in ["11", "00"])
        c3 = int(s, 8) % 5 == 0
        if c1 and c2 and c3:
            c += 1

print(c)