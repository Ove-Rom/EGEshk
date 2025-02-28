def div(x):
    ans = set()
    for i in range(2, round(x ** .5) + 1):
        if x % i == 0:
            ans |= {i, x // i}
    ans = sorted(ans)
    if ans: return ans[-1] + ans[-2]
    return 0


def simp(x):
    for i in range(2, round(x ** .5)):
        if x % i == 0:
            return 0
    return 1

for n in range(112_500_000, 112_550_001):
    if not simp(n):
        m = div(n)
        if str(m)[-4:] == "1214":
            print(n)
