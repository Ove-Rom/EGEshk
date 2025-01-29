def f(a):
    for x in range(1000):
        for y in range(1000):
            f1 = (x + y <= 30) or (y <= x + 2) or (y >= a)
            if not f1: return 0
    else: return 1

for a in range(1000, 0, -1):
    if f(a):
        print(a)
        break