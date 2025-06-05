def div(x):
    ans = set()
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            d1 = i
            d2 = x // i
            if str(d1)[-1] == "7" and d1 != x and d1 != 7: ans.add(d1)
            if str(d2)[-1] == "7" and d2 != x and d2 != 7: ans.add(d2)
    if ans:
        return min(ans)
    return 0


c = 0

for i in range(700_000, 10 ** 10):
    if d := div(i):
        print(i, d)
        c += 1
        if c == 5: break
