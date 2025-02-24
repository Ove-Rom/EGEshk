from itertools import product

for v in "0123456789":
    for i in range(4):
        for z in product("0123456789", repeat=i):
            num = f"1{v}2139{''.join(z)}4"
            if int(num) % 3052 == 0:
                print(num, int(num) // 3052)