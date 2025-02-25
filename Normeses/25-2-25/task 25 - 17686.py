def div(x):
    ans = set()
    for i in range(1, round(x ** 0.5) + 1):
        if x % i == 0:
            ans |= {i, x // i}
    return ans


def isP(x):
    if x == 1: return 0
    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            return 0
    return 1


def P(x):
    divs = div(x)
    s = [i for i in divs if isP(i)]
    return [len(s), sum(s)]


def E(x):
    divs = div(x)
    s = [i for i in divs if i % 2 == 0]
    return [len(s), sum(s)]


c = 0

for i in range(100_000_001, 10 ** 10):
    lp, p = P(i)
    le, e = E(i)
    if lp == le:
        print(i, abs(p - e))
        c += 1
        if c == 5: break
