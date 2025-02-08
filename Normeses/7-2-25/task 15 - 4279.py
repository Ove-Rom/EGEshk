for a in range(1, 1000):
    if all((x & 1097 == 0) <= ((x & 2047 != 0) <= (x & a != 0)) for x in range(1, 100000)):
        print(a)
        break