def div(x):
    ans = set()
    for i in range(2, round(x) + 1):
        if x % i == 0:
            if str(i)[-1] == '9' and i != 9: ans.add(i)
            if str(x // i)[-1] == '9'and x // i != 9: ans.add(x // i)
    if ans: return min(ans)
    return 0

c = 0

for i in range(800_000, 10 ** 10):
    d = div(i)
    if d:
        print(i, d)
        c += 1
        if c == 5: break
