def div(x):
    ans = set()
    for i in range(2, round(x ** .5) + 1):
        if x % i == 0:
            if simp(i): ans.add(i)
            if simp(x // i): ans.add(x // i)
    if ans: return min(ans)+ max(ans)
    return 0


def simp(x):
    for i in range(2, round(x ** .5)):
        if x % i == 0:
            return 0
    return 1


c = 0

for i in range(1_200_001, 10 ** 10):
   m = div(i)
   if m > 2000 and m % 10 == 8:
       print(i, m)
       c += 1
       if c == 5: break