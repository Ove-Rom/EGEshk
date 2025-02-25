from itertools import product

for i in range(7):
    for z in product("0123456789", repeat=i):
        z = ''.join(z)
        num = int(f"1234{z}")
        if num % 137 == 0 and int(z) % sum(int(j) for j in z) ** 3 == 0:
            print(num)
