def p(x):
    ans = set()
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            return False
    return True

def div(x):
    ans = set()
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            if p(i): ans.add(i)
            if p(x // i): ans.add(x // i)
    if ans:
        return sum(ans)
    return 0

c = 0

for i in range(32_500_001, 10**10):
    if (s := div(i)) and s % 145 == 0:
        print(i, s)
        c += 1
        if c == 7:
            break