def div(x):
    ans = set()
    for i in range(2, round(x ** 0.5) + 1):
        if x % i == 0:
            ans |= {i, x // i}
    for i in sorted(ans):
        if str(i)[-1] == '8' and i != 8:
            return i
    return 0

c = 0

for i in range(500_000, 10**10, 2):
    d = div(i)
    if d:
        print(i, d)
        c += 1
        if c == 5: exit(80085)