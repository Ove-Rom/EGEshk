for a in range(1000, -1000, -1):
    if all((x % 7 == 0) or (x % 13) or (x > a - 40) for x in range(1000)):
        print(a)
        break