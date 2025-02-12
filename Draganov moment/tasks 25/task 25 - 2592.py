def div(x):
    ans = set()
    for i in range(2, round((x ** 0.5) + 1)):
        if x % i == 0:
            ans.add(i)
            ans.add(x // i)
    return sorted(ans)

def p(x): return x != 1 and not div(x)

L = 55_000_000
R = 60_000_000
r = round(R ** 0.25)
ans = []

for i in range(2, r+1):
    if p(i):
        n = i ** 4
        while n <= R:
            if L <= n: ans.append([n, i ** 4])
            n *= 2

for i in sorted(ans): print(*i)