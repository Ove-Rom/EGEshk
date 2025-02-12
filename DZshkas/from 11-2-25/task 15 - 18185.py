for a in range(1000, -1000, -1):
    if all(((x % 7) and (x % 17 == 0)) <= (x > a - 40) for x in range(1000)):
        print(a)
        break