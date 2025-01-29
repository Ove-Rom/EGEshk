def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            f1 = (x < a) or (y < a) or (x + 2*y > 50)
            if not f1: return 0
    else: return 1

for a in range(1000):
    if f(a):
        print(a)
        break