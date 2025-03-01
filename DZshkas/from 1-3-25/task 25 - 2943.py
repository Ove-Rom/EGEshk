def div(x):
    for i in range(2, round(x ** .5) + 1):
        if x % i == 0:
            return i + x // i
    return 0

c = 0

for i in range(220_001, 10**10):
    m = div(i)
    if str(m)[-1] == '4':
        print(i, m)
        c += 1
        if c == 5: break