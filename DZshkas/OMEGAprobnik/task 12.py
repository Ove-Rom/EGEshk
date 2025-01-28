for i in range(2, 333):
    if all(i % x != 0 for x in range(2, i)) and (43+i) % i == 0:
        print(i)