def f(a):
    for x in range(1000):
            for y in range(1000):
                f1 = (x + 2*y > a) or (y < x) or (x<30)
                if not f1:
                    return 0
    else: return 1

for a in range(1000, 0, -1):
    if f(a):
        print(a)
        break