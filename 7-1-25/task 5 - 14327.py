for n in range(100000, 0, -1):
    r = oct(n)[2:]
    if n % 2 == 0:
        r += str(max(int(i) for i in r))
    else:
        r += oct(min(int(i) for i in r) * 2)[2:]
    r = int(r, 8)
    if r < 313:
        print(n)
        break