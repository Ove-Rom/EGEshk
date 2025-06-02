def toq(a, q):
    ans = ''
    while a:
        ans += str(a % q)
        a //= q
    return ans[::-1]


for n in range(1000, 0, -1):
    r = toq(n, 3)
    if n % 3 == 0:
       r = "1" + r + "02"
    else:
        r += toq(n % 3 * 4, 3)
    r = int(r, 3)
    if r < 199:
        print(n)
        break