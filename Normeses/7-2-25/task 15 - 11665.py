for a in range(1000):
    if all((a+x > 700-a) and ((a % 100) + (100 % x) > 50) for x in range(1,1000)):
        print(a)
        break