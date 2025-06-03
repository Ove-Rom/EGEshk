from itertools import product, repeat

count = 0

for i in product("0123456789ABCDE", repeat=5):
    s = "".join(i)
    c1 = s.count("8") == 1
    c2 = sum(int(j, 15) > 9 for j in s) >= 2
    if c1 and c2:
        count += 1

print(count)