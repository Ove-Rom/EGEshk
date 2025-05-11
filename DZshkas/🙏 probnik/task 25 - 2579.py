def div(x):
    ans = set()
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            ans |= {i, x // i}
    if len(ans) < 3: return 0
    s = sum(sorted(list(ans))[-3:])
    if s ** .5 == int(s ** .5):
        return s
    return 0

c = 0

for i in range(10_000_001, 10**10):
    if s := div(i):
        print(s)
        c += 1
        if c == 5: break
