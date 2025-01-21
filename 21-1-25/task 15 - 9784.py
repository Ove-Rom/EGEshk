def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f1 = (x * y < a) or (x < y) or (9 < x)
            if not f1: return 0
    else: return 1

for a in range(1000):
    if f(a):
        print(a)
        break