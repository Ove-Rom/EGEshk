for n in range(2, 10**10):
    r = f"{n:b}"
    c1 = sum(j == "1" for j in r[1:2])
    c0 = sum(j == "0" for j in r[::2])
    r = abs(c1 - c0)
    if r == 5:
        print(n)
        break