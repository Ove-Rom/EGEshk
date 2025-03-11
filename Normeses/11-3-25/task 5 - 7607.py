for n in range(10**10):
    r = bin(n)[2:]
    if n % 3 == 0:
        r += r[-3:]
    else:
        r += bin(n % 3 * 3)[2:]
    r = int(r, 2)
    if r > 76:
        print(n)
        break