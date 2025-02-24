from itertools import product

ans = []

for v1 in "1234567890":
    for v2 in "1234567890":
        for v3 in "1234567890":
            for i in range(3):
                for z in product("0123456789", repeat=i):
                    num = int(f"12{''.join(v1)}3{''.join(z)}456{''.join(v2)}{''.join(v3)}9")
                    # print(num)
                    if num % 98591 == 0:
                        ans.append((num, num // 98591))

for i in sorted(ans):
    print(*i)