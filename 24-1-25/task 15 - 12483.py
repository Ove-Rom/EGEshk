for a in range(100):
    if all(not(x & 79 == 0) and ((x&31 == 0) <= ((x&a)!=0)) for x in range(90, 101)):
        print(a)
        break