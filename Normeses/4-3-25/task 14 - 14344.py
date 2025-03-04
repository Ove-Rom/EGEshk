for p in range(16, 37):
    n1 = int("17496", p)
    n2 = int("91f83", p)
    n3 = int("d9543", p)
    s = n1 + n2 + n3
    if s % 12 == 0:
        print(s // 12)
        break