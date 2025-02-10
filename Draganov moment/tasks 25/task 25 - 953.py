def div(x):
    ans = set()
    for i in range(2, round(x ** 0.5)+1):
        if x % i == 0:
            ans.add(i)
            ans.add(x // i)
    return sorted(ans)


def isP(x): return x > 1 and not div(x)


# pDivs = [i for i in range(round(500000 ** 0.5 + 1)) if isP(i)]
count = 0
# print(div(20))

for i in range(499999, 0, -1):
    s = sum(j for j in div(i) if isP(j))
    if s and s % 10 == 0:
        count += 1
        print(i, s)
        if count == 7: break
