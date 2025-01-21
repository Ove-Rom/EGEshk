def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f1 = (2*x + y != 70) or (x < y) or (a < x)
            if not f1: return 0
    else: return 1

for a in range(100, 0, -1):
    if f(a):
        print(a)
        break