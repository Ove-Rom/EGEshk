def div(x):
    ans = set()
    for i in range(1, round(x**0.5)):
        if x % i == 0:
            ans |= {i, x // i}
    for i in sorted(ans):
        if str(i)[-1] == '7' and i != 7:
            return i
    return 0

c = 0

for i in range(700_001, 10**10):
    d = div(i)
    if d:
        print(i, d)
        c += 1
        if c == 5: break