for x in range(149, -1, -1):
    n1 = 5*150**4 + 150**3 + x*150**2 + 2*150 + 9
    n2 = x*150**3 + 2*150 + 3
    n = n1 + n2
    if n % 149 == 0:
        print(n // 149)
        break