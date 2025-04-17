for n in range(1, 10 ** 5):
    r = f"{int(n):b}"
    r = "1" + "".join(str(int(not int(i))) for i in r)
    if r.count("1") % 2 == 0:
        r += "0"
    else: r += "1"
    r = int(r, 2)
    if r > 180:
        print(n)
        break