for a in range(10000, 0, -1):
    if all((x % a) <= (x % 14) or (x % 4) for x in range(1000)):
        print(a)
        break