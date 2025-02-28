def div(x):
    ans = set()
    for i in range(2, round(x ** .5)):
        if x % i == 0:
            ans |= {i, x // i}
    if len(ans) >= 7: return [sorted(ans)[-7], len(ans)]
    return 0

c = 0

for i in range(400_000_001, 10**10):
    d = div(i)
    if d:
        print(*d)
        c += 1
        if c == 5: break