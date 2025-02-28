def simp(x):
    for i in range(2, round(x ** .5)):
        if x % i == 0:
            return 0
    return 1


c = 0

for i in range(600_001, 10 ** 10):
    n1 = i - 1
    n2 = i + 1
    if i % 6 == 0 and simp(n1) and simp(n2):
        print(n1, n2)
        c += 1
        if c == 6: break
