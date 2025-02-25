def div(x):
    for i in range(2, round(x) + 1):
        if x % i == 0 and str(i + x // i)[-1] == '4':
            return i + x // i
    return 0

c = 0

for i in range(800_000, 10**10):
    m = div(i)
    if m:
        print(i, m)
        c += 1
        if c == 5: break