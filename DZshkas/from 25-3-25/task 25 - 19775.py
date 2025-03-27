def isP(x):
    for i in range(2, round(x ** .5) + 1):
        if x % i == 0: return 0
    return 1


def div(x):
    ans = {0}
    for i in range(2, round(x ** .5) + 1):
        if x % i == 0:
            if isP(i): ans.add(i)
            if isP(x // i): ans.add(x // i)
    return sum(ans)


c = 0

for i in range(32_500_001, 10 ** 10):
    s = div(i)
    if s and s % 145 == 0:
        print(i, s)
        c += 1
        if c == 7: break
