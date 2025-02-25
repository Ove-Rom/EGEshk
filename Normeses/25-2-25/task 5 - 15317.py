for n in range(1, 10**10):
    r = bin(n)[2:]
    if n % 2 == 0:
        r += "01"
    else:
        r = '1' + r + '1'
    r = int(r, 2)
    if r > 156:
        print(n)
        break