for n in range(4, 10_000):
    s = "1" + "8" * n
    while any(i in s for i in ["18", "388", "888"]):
        s = s.replace("18", "8", 1)
        s = s.replace("388", "81", 1)
        s = s.replace("888", "3", 1)
    if s.count("1") == 3:
        print(n)
        break