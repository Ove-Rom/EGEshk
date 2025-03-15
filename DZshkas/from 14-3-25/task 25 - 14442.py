from fnmatch import fnmatch


def div(x):
    ans = set()
    for i in range(1, round(x ** .5) + 1):
        if x % i == 0:
            if fnmatch(str(i), "*7?"):
                ans.add(i)
            if fnmatch(str(x // i), "*7?"):
                ans.add(x // i)
    if len(ans) >= 18: return sum(ans)
    return 0


for i in range(400_000, 500_001):
    d = div(i)
    if d:
        print(i, d)
