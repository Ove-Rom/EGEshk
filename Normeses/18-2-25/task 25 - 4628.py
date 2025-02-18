for i in range(1234065, 10 ** 8, 161):
    m1 = str(i)[:2] == "12"
    m2 = str(i)[-4] == '4'
    m3 = str(i)[-2:] == "65"
    if m1 and m2 and m3 and i % 161 == 0:
        print(i, i // 161)