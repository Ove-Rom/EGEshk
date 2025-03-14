for i in range(4, 10000):
    s = '2' + '5' * i
    while "25" in s or "355" in s or "555" in s:
        s=s.replace("25", '5')
        s=s.replace("355", "552")
        s=s.replace("555", '3')
    if s.count('2') == 10:
        print(i)
        break