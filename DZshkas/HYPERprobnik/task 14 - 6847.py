for x in range(110, 0, -1):
    n1 = x * 1000 + 3 * 111**2 + 2 * 111 + 1
    n2 = 211**3 + 7 * 211**2 + x * 10 + 4
    n = n1 + n2
    if n % 111 == 0:
        print(n // 111, x)
        break