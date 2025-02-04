for a in range(1000000):
    if all((y > 10) or (x*a > y+x) for x in range(1, 10000) for y in range(1, 10000)):
        print(a)
        break