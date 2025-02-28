from itertools import product

c = 0

for i in product("kotbus", repeat = 8):
    s = ''.join(i)
    if s[0] not in "ou" and "kot" in s:
        c += 1

print(c)