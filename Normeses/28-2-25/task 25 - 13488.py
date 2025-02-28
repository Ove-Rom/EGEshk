def div(x):
    ans = set()
    for i in range(2, round(x ** .5)):
        if x % i == 0:
            if i % 2: ans.add(i)
            if (x // i) % 2: ans.add(x // i)
    if len(ans) == 3: return sorted(ans)
    return 0


for i in range(18_782, 18_823):
    d = div(i)
    if d:
        print(*d)
