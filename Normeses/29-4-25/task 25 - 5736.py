def div(x):
    for i in range(2, int(x ** .5) + 1):
        if x % i == 0:
            if x // i % 7 == 0:
                return x // i
            return False
    return False


c = 0

for i in range(10 ** 9 + 1, 10 ** 10):
    s = str(i)
    if s == s[::-1]:
        if d := div(i):
            print(i, d)
            c += 1
            if c == 5: break