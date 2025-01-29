def f(a):
    for x in range(1000):
        for y in range(1000):
            f1 = not ((x < 7) or (y >= 3*x + a - 20) or (x >= 34) or (y < 121))
            if f1: return 1
    else:return 0

for a in range(1000)[::-1]:
    if not f(a):
        print(a)
        break