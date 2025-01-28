def f(a):
    for x in range(1000):
        f1 = ((x % 10 == 0) and (x % 26 == 0) and (x >= 300)) <= (a <= x)
        if not f1:
            return 0
    else: return 1
for a in range(1000, 0, -1):
    if f(a):
        print(a)
        break