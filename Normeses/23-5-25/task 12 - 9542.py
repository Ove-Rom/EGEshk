for n in range(101, 10**10):
    s = n * "5"
    while "555" in s or "11" in s or "2" in s:
        s = s.replace("555", "1", 1)
        s = s.replace("11", "25", 1)
        s = s.replace("2", "5", 1)
    if s == "15":
        print(n)
        break