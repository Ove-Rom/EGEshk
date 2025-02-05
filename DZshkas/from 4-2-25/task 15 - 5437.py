for a in range(200, 0, -1):
    if all(((z % 115 == 0) or
           (y % 78 == 0) or
           (x % 51 == 0)) <=
           (x % a == 0)
           for x in range(1000)
           for y in range(1000)
           for z in range(1000)):
        print(a)
        break
