for a in range(1_000, 0, -1):
    if all((x + 2*y > a) or (y < x) or (x < 30) for x in range(1, 1_000) for y in range(1, 1_000)):
        print(a)
        break