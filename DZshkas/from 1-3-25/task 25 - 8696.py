def div(x):
    ans = set()
    for i in range(2, round(x ** .5) + 1):
        if x % i == 0:
            ans |= {i, x // i}
    return sum(ans)

def simp(x):
    for i in range(2, round(x ** .5) + 1):
        if x % i == 0:
            return 0
    return 1

c = 0

for i in range(1_273_547, 10**10):
    if not simp(i):
        m = div(i)
        if simp(m % 100_000):
            print(i, m)
            c += 1
            if c == 5: break