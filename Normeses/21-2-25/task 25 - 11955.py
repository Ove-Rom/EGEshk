for i in range(1021706, 10 ** 10, 133):
    s = str(i)
    c1 = s[0] == "1"
    c2 = int(s[1]) % 2 == 0
    c3 = s[2:6] == "2157"
    c4 = all(int(j) % 2 != 0 for j in s[6:-1])
    c5 = s[-1] == '4'
    if c1 and c2 and c3 and c4 and c5:
        print(i, i // 133)
