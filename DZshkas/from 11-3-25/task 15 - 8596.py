for a in range(10000):
    if all((x >= 11) or (3 * x < y) or (x * y < a) for x in range(1000) for y in range(1000)):
        print(a)
        break