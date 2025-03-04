def toq(a, q):
    ans = ''
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]

for n in range(1000, 0, -1):
    r = toq(n, 7)
    if n % 2 == 0: r = "52" + r + '1'
    else: r = r[-1] + r[1:-1] + r[0] + "15"
    r = r.strip('0')
    if len(r) == 4:
        print(n)
        break