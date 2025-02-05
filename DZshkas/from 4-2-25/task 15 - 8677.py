for a in range(1000, 0, -1):
    if all((x% 17 == 0) <= (not (80 <= x <= 100) or (a < x + 30)) for x in range(1000)):
        print(a)
        break
