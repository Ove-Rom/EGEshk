from itertools import product

ans = []

for v in "123456":
    for i in range(4):
        for z in product("0123456", repeat=i):
            num = int(f"{v}213{''.join(z)}5664", 7)
            if num % 333 == 0 and num < 10**9:
                ans.append((num, num // 333))

for i in sorted(ans):
    print(*i)
