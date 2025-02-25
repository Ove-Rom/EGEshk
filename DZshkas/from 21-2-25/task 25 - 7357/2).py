from itertools import product

c = 0
ans = []

for v in "2468":
    for vKon in " 13579":
        for i in range(6):
            for z in product("1234567890", repeat=i):
                num = int(f"{v}136{''.join(z)}{vKon}")
                if num % 53191 == 0:
                    ans.append((num, num // 53191))

for j in sorted(ans)[::-1][:5][::-1]:
    print(*j)

