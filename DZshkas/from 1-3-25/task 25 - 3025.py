def div(x):
    ans = set()
    for i in range(2, round(x ** .5) + 1):
        if x % i == 0:
            if i % 2: ans.add(i)
            if (x // i) % 2: ans.add(x // i)
    if len(ans) >= 6: return sorted(ans)[-6]
    return 0


c = 0

for i in range(200_000_001, 10 ** 10):
    d = div(i)
    if d:
        print(i, d)
        c += 1
        if c == 5: break
