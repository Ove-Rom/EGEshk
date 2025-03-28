def isP(x):
    for i in range(2, round(x ** .5) + 1):
        if x % i == 0: return 0
    return 1

def div(x):
    ans = {0}
    for i in range(2, round(x ** .5) + 1):
        if x % i == 0:
            ans.add(x // i)
            ans.add(i)
    return sum(ans)

c = 0

for i in range(1_273_548, 10**10):
    m = div(i)
    if m and isP(m % 100_000):
        print(i, m)
        c += 1
        if c == 5: break