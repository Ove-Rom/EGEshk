def div(x):
    ans = set()
    for i in range(2, int(x**.5) + 1):
        if x % i == 0:
            ans |= {i, x//i}
    if not ans: return 0
    return sum(ans) // len(ans)

c = 0

for i in range(700_000, 0, -1):
    if str(m:=div(i))[-3:] == "313":
        print(i, m)
        c += 1
        if c == 7: break