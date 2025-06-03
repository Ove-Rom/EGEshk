from itertools import product

count = 0

for i in product("дгиашэ", repeat=5):
    s = "".join(i)
    c1 = s[0] not in "иаэ"
    c2 = s[-1] not in "дгш"
    if c1 and c2:
        count += 1

print(count)