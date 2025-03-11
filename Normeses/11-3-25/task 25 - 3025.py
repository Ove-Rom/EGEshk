def div(x):
    ans = set()
    for i in range(2, round(x ** .5) + 1):
        if x % i == 0:
            if i % 2: ans |= {i}
            if x // i % 2: ans |= {x // i}
    ans = sorted(ans)
    if len(ans) < 6:
        return 0
    return ans[-6]

c = 0

for i in range(200_000_001, 10**13):
    d = div(i)
    if d:
        print(i, d)
        c += 1
        if c == 5:
            break