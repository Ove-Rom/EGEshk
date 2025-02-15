for a in range(10000):
    if all((x%31 != 0) or (x & a != 0)\
           for x in range(90, 101)):
        print(a)
        break