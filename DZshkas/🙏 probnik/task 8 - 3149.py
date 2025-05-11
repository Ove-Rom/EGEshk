from itertools import product

trip = [i*3 for i in "0123456789"]
c = 0

for i in range(10000, 100000):
    i = str(i)
    if i[-1] in "347": continue
    if not any(j in "".join(i) for j in trip):
        c += 1

print(c)