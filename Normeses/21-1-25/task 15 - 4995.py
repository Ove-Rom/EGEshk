def f(a):
    ans = []
    for x in range(1, 1000):
            for y in range(1, 1000):
                f1 = (x + y <= 22) or (y <= x - 6) or (y >= a)
                if not f1: return 0
    else: return 1

for a in range(1000, 0, -1):
    if f(a):
        print(a)
        break