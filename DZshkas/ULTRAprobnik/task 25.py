for i in range (121025674, 10**10, 7777):
    s = str(i)

    m1 = s[:2] == "12"
    m2 = s[-4:-1] == "567"

    c1 = i % 7777 == 0
    c2 = i % 2 == 0

    if m1 and m2 and c1 and c2: print(i, i // 7777)