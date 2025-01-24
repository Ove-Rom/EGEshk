def toq(a, q):
    ans = ''
    while a:
        ans += str(a%q)
        a //= q
    return ans[::-1]

ans = []

for n in range(1000):
    r = toq(n, 3)
    s = sum(int(i) for i in r)
    if s % 3 == 0:
        r = '20' + r
    else:
        r = '10' + r
    if int(r, 3) < 100:
        ans.append(n)

print(max(ans))