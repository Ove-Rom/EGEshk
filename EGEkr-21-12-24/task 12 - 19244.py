for n in range(3, 10000000):
    r = '1' + '2' * n
    while "12" in r or "322" in r or "222" in r:
        if "12" in r:
            r = r.replace("12", '2', 1)
        if "322" in r:
            r = r.replace("322", "21", 1)
        if "222" in r:
            r = r.replace("222", '3', 1)
    if sum(int(i) for i in r) == 15:
        print(n)
        break