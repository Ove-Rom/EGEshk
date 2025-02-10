def div(x):
    ans = set()
    for i in range(2, round(x ** 0.5)):
        if x % i == 0:
            ans.add(i)
            ans.add(x // i)
    return sorted(ans)


cnt = 0
for i in range(500_000, 10 ** 10):
    divs = div(i)
    divs8 = [j for j in divs if str(j)[-1] == "8" and j != 8]
    if divs8:
        print(i, divs8[0])
        cnt += 1
        if cnt == 5: break
