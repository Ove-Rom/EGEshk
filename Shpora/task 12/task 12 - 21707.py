for n in range(4, 10_000):
    s = "4" + "2" * n
    while any(i in s for i in ["42", "8222", "2222"]):
        s = s.replace("42", "2", 1)
        s = s.replace("8222", "24", 1)
        s = s.replace("2222", "8", 1)
    if sum(map(int, s)) == 110:
        print(n)
        break