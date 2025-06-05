def div(x):
    ans = set()
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            ans |= {i, x // i}
    if ans:
        return min(ans) + max(ans)
    return 0

c = 0

for i in range(700_001, 10**10):
    if str(m := div(i))[-1] == "4":
        print(i, m)
        c += 1
        if c == 5: break