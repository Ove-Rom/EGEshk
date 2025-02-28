def div(x):
    ans = set()
    for i in range(2, round(x ** .5) + 1):
        if x % i == 0:
            if simp(i): ans.add(i)
            if simp(x // i): ans.add(x // i)
    if ans: return sum(ans) // len(ans)
    return 0


def simp(x):
    for i in range(2, round(x ** .5)):
        if x % i == 0:
            return 0
    return 1


c = 0

for i in range(650_001, 10 ** 10):
   f = div(i)
   if f % 37 == 23:
       print(i, f)
       c += 1
       if c == 4: break