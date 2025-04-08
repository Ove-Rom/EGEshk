from itertools import product

c = 0

for i in product("dgiase", repeat = 5):
    c1 = i[0] not in "iae"
    c2 = i[-1] not in "dgs"
    if not (c1 or c2): c += 1

print(c)