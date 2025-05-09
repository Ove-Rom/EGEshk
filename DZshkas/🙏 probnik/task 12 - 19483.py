for n in range(4, 10_000):
    s = "2" + "5" * n
    while any(j in s for j in ["25", "355", "555"]):
        s = s.replace("25", "5", 1)
        s = s.replace("355", "522", 1)
        s = s.replace("555", "3", 1)
    if s.count("2") == 10:
        print(n)
        break