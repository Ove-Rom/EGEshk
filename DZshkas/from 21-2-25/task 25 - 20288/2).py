from itertools import product

for i in range(6):
    for z in product("02468", repeat=i):
        for v1 in "13579":
            for v2 in "13579":
                num = int(f"{''.join(z)}12{''.join(v1)}4{''.join(v2)}")
                if num % 9231 == 0 and str(num)[0] != '0':
                    print(num, num // 9231)
