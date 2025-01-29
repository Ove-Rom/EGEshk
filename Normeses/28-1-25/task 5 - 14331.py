def toq(a, q):
    ans = ''
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]

ans = []
for n in range(1000):
    r = toq(n, 3)
    s = sum(int(i) for i in r)
    if s % 3 == 0:
        r += "212"
    else:
        r += toq(s * 2, 3)
    r = int(r, 3)
    if r > 490: ans.append(r)

print(min(ans))