for a in range(1000):
    if all((x & 57 == 0) or ((x & 23 == 0) <= (not (x & a == 0))) for x in range(1000)):
        print(a)
        break
