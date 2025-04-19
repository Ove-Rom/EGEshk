def div(x):
    ans = {0}
    for i in range(2, round(x ** .5) + 1):
        if x % i ==0:
            ans |= {i, x //i}
    return sum(ans)

def isP(x):
    if x in [0, 1]: return False
    for i in range(2, round(x ** .5) + 1):
        if x % i == 0:
            return False
    return True

c = 0

for i in range(1_273_547, 10**10):
    m = div(i)
    if isP(m % 100_000):
        print(i, m)
        c += 1
        if c == 5: break