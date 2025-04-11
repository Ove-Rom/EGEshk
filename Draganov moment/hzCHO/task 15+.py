for a in range(100000):
    if all((9*x + y > a) or (x >= 36) or (y >= 18) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)