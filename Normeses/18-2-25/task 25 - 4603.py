for i in range(1234737, 10 ** 8, 141):
    m1 = str(i)[:4] == "1234"
    m2 = str(i)[-1] == '7'
    if m1 and m2 and i % 141 == 0:
        print(i, i // 141)
