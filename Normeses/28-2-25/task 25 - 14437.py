def div(x):
    ans = set()
    for i in range(2, round(x ** .5) + 1):
        if x % i == 0:
            ans |= {i, x // i}
    ans = sorted(ans)
    if ans: return sum(ans) // len(ans)
    return 0

c = 0

for i in range(700_000)[::-1]:
    m = div(i)
    if m:
        if str(m)[-3:] == "313":
            print(i, m)
            c += 1
            if c == 7: break