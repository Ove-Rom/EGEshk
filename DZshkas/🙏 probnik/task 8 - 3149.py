from itertools import product

trip = [i*3 for i in "0123456789"]
c = 0

for i in product("0123456789", repeat=5):
    if i[-1] in "347": continue
    if not any(j in "".join(i) for j in trip):
        c += 1

print(c)