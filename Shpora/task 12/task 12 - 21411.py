for n in range(4, 10_000):
    s = "3" + "1" * n
    while any(i in s for i in ["31", "211", "1111"]):
        s = s.replace("31", "1", 1)
        s = s.replace("211", "13", 1)
        s = s.replace("1111", "2", 1)
    if sum(map(int, s)) == 15:
        print(n)
        break