def f(a):
    for x in range(1000):
        for y in range(1000):
            f1 = (x**2 + y**2 > 1024 - x) or (y < (-2) * x + a)
            if not f1: return 0
    else: return 1

count = 0

for a in range(1000):
    if f(a):
        print(a)
        break