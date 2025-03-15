from fnmatch import fnmatch


def div(x):
    ans = set()
    for i in range(1, round(x ** .5) + 1):
        if x % i == 0:
            if i % 2 == 0: ans.add(i)
            if x // i % 2 == 0: ans .add(x // i)
    if len(ans) >= 4: return sum(ans)
    return 0

c = 0

for i in range(65001, 10**10):
    d = div(i)
    if d and fnmatch(str(i), "6*97*5?"):
        print(i, d)
        c += 1
        if c == 7: break
