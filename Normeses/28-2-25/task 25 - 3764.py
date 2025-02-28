def div(x):
    ans = set()
    for i in range(1, round(x ** .5) + 1):
        if x % i == 0:
            ans |= {i, x // i}
    return sum(i % 2 == 0 for i in ans)

c = 0

for k in range(10**10):
    n = div(k + 750_000)
    if n % 2:
        print(k, n)
        c += 1
        if c == 5: break