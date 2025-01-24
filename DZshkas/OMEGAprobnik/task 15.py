for a in range(0, -1000, -1):
    if all(((x * y < a+13)) <=
           ((28 * y > 520) or
            (x * 25 > 800))
           for x in range(10000) for y in range(10000)):
        print(a)
        break