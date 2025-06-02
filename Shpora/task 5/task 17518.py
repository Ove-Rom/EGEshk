for n in range(1, 1000):
    r = f"{n:b}"
    if r.count("1") % 2 == 0:
        r += "0"
        r = "10" + r[2:]
    else:
        r += "1"
        r = "11" + r[2:]
    r = int(r, 2)
    if r > 50:
        print(n)
        break