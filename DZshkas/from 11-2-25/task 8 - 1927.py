from itertools import product

count = 0

for i in product("ясновидец", repeat=5):
    if i[0] in "снвдц" and i[-1] in "яоие":
        if i.count(i[0]) == 1 == i.count(i[-1]):
            count += 1

print(count)
