for b in range(1000):
    if all(((x & 500 != 0) and (x & 200 == 0)) <= (not(x & b == 0)) for x in range(1000)):
        print(b)
        break